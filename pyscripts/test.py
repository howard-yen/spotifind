from parse import *
from getinfo import *

auth = 'BQC8Ez1MxOcOTASDHdE1h22PP2nG4GREwjKjSnW7nBx547pfrm-bbu0OJc_CFg1Fm91oeNRHvF99tXXThNxwi2C9F1fV1nRIKWMPGLLpdPy4pHUNvvMZAyfWwGfF2Ul3v5x9pv9Yn8s-NRfCWCQB8PwZitnbaSi-fwcggFx_aoI'
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
# save data
combined_vector = np.expand_dims(combined_vector, axis=0)
np.savetxt('user_vectors.csv', combined_vector, delimiter=',')
# load data
my_data = np.genfromtxt('user_vectors.csv', delimiter=',')
print(my_data)
print(my_data.shape)
