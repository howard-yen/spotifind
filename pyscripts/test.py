from parse import *
from getinfo import *

auth = 'BQCMqQfNMm7r_ngkXeWwJWdWDJ6hyCRAO-0g7EHuC1K80sqbhtxal2emzud00JwvXLvo_3X4DvNXRqX6_1nUcej2TjRgiSrXvivP_SRxFcB6siy1Y_gTCTYKJaCJ6HFn7dFyFdgGobyxuyr-aZ23_UTXsCczEgDMvw4H_0vSff0'
dct = read_genres()
t = get_top_tracks_features(auth)
track_vector = parse_track_features(t)
print(track_vector)
print(track_vector.shape)
t = get_top_artists_genres(auth)
genre_vector = parse_genres(t, dct)
print(genre_vector)
print(genre_vector.shape)
combined_vector = combine_vectors(track_vector, genre_vector)
print(combined_vector)
print(combined_vector.shape)
