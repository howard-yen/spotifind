import pandas as pd
import numpy as np
import scipy.sparse
from .getinfo import *

genre_dict = dict()

def read_genres():
    genre_csv = pd.read_csv('genres.csv')

    nums = genre_csv['number'].to_numpy()
    genre = genre_csv['genre'].to_numpy()

    for i in nums:
        genre_dict[genre[i-1]] = i

    return genre_dict

def update_db(clients, clients_location):
    userdata = pd.read_csv('userdata.csv')
    clients2 = clients.copy()
    ids = userdata['user_id'].to_numpy()
    for i, user_id in enumerate(ids):
        if not user_id in clients:
            userdata.drop([i])
        else:
            del clients2[user_id]

    newclients = []
    for i in clients2:
        token = clients[i]
        top_tracks = get_top(token)
        tracks = get_features_from_tracks(token, top_tracks)
        artists = get_top_artists_genres(token)

        track_feats = parse_track_features(tracks)
        genre_feats = parse_genres(artists)
        full_feats = combine_vectors(track_feats, genre_feats)
        newclients.append([i] + [clients[i]] + [clients_location[i]['lat'], clients_location[i]['lon']] + full_feats.tolist())

    for i in range(len(newclients)):
        userdata.loc[i] = newclients[i]

    # print(userdata.to_csv(index=False))
    with open('userdata.csv', 'w') as f:
        userdata.to_csv(f, index=False)

# input the top tracks from spotify api
# return a 1d array of the average track features
def parse_track_features(tracks):
    audio_features = tracks['audio_features']
    feature_vec = np.zeros((len(audio_features), 8))

    for i, row in enumerate(audio_features):
        feature_vec[i, 0] = row['danceability']
        feature_vec[i, 1] = row['energy']
        feature_vec[i, 2] = row['loudness']
        feature_vec[i, 3] = row['speechiness']
        feature_vec[i, 4] = row['acousticness']
        feature_vec[i, 5] = row['instrumentalness']
        feature_vec[i, 6] = row['liveness']
        feature_vec[i, 7] = row['valence']

    return feature_vec.mean(0)

def parse_genres(artists):
    genre_vec = np.zeros((1000))
    for artist in artists:
        for genre in artist:
            if genre in genre_dict:
                genre_vec[genre_dict[genre]-1] += 1
    #genre_csr = scipy.sparse.csr_matrix(genre_vec)

    return genre_vec

def combine_vectors(song_vector, genre_vector):
    #combined = scipy.sparse.hstack([song_vector, genre_vector])
    combined = np.append(song_vector, genre_vector)
    return combined

def get_neighbor_ids(indices):
    user_ids = pd.read_csv('user_ids.csv')
    user_ids = user_ids['user_id'].to_numpy()
    nbr_ids = []
    for i, row in enumerate(indices):
        nbr_ids.append([])
        for idx in row:
            nbr_ids[i].append(user_ids[idx])
    return nbr_ids
