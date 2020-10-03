from parse import *
from getinfo import *

auth = 'BQBmJX3eD1f_2hLKwoaLJ7uk3GBiea2JuHq8QV5MxFQwzv8oLLlpkMnGVayUbvTNSFG3pWCkXK66VgrmvQVk7ARrrqVBEhq-mn3ehD3m7FCRM3SlRV7CAbHkBCIOFkHFxP2CDSh3wqjZEPZrzB_2yNqzvEUjPKsD23AlaZs7QFU'
dct = read_genres()
t = get_top_tracks_features(auth)
print(parse_track_features(t))
t = get_top_artists_genres(auth)
print(parse_genres(t, dct))
