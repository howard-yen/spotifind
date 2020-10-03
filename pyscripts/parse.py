import pandas as pd
import numpy as np
import scipy.sparse

def read_genres():
    genre_csv = pd.read_csv('genres.csv')

    nums = genre_csv['number'].to_numpy()
    genre = genre_csv['genre'].to_numpy()

    genre_dict = dict()
    for i in nums:
        genre_dict[genre[i-1]] = i

    return genre_dict

# input the top tracks from spotify api
# return a 1d array of the average track features
def parse_track_features(track):
    audio_features = track['audio_features']
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

    return feature_vec.mean(0)[0]

def parse_genres(artists, genre_dict):
    genre_vec = np.zeros((1000))
    for artist in artists:
        for genre in artist:
            if genre in genre_dict:
                genre_vec[genre_dict[genre]-1] += 1 
    genre_csr = scipy.sparse.csr_matrix(genre_vec)

    return genre_csr

def combine_vectors(song_vector, genre_vector):
    combined = scipy.sparse.hstack([song_vector, genre_vector])

    return combined
