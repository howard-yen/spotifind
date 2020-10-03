from parse import *
from getinfo import *

auth = 'BQCMqQfNMm7r_ngkXeWwJWdWDJ6hyCRAO-0g7EHuC1K80sqbhtxal2emzud00JwvXLvo_3X4DvNXRqX6_1nUcej2TjRgiSrXvivP_SRxFcB6siy1Y_gTCTYKJaCJ6HFn7dFyFdgGobyxuyr-aZ23_UTXsCczEgDMvw4H_0vSff0'
dct = read_genres()
t = get_top_tracks_features(auth)
print(parse_track_features(t))
t = get_top_artists_genres(auth)
print(parse_genres(t, dct))
