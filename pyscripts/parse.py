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

def parse_track_features(track):
    audio_features = track['audio_features'][0]
    feature_vec = np.zeros((9))
    feature_vec[0] = audio_features['danceability']
    feature_vec[1] = audio_features['energy']
    feature_vec[2] = audio_features['loudness']
    feature_vec[3] = audio_features['speechiness']
    feature_vec[4] = audio_features['acousticness']
    feature_vec[5] = audio_features['instrumentalness']
    feature_vec[6] = audio_features['liveness']
    feature_vec[7] = audio_features['valence']
    feature_vec[8] = audio_features['tempo']
    return feature_vec

def parse_genres(artists, genre_dict):
    genre_vec = np.zeros((1000))
    for artist in artists:
        for genre in artist:
            if genre in genre_dict:
                genre_vec[genre_dict[genre]] += 1 
    genre_csr = scipy.sparse.csr_matrix(genre_vec)

    return genre_csr
