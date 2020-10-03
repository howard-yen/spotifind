import pandas as pd
import numpy as np

def read_genres():
    genres_csv = pd.read_csv('genres.csv')
    
    nums = genres_csv['number'].to_numpy()
    genre = genres_csv['genre'].to_numpy()
    
    genres_dict = dict()
    for i in nums:
        genres_dict[genre[i-1]] = i 

    return genres_dict

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
