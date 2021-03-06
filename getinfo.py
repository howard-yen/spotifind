import requests

def get_top(auth, tracks=True):
    url = 'https://api.spotify.com/v1/me/top/{}'
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json', 'Authorization': 'Bearer {}'.format(auth)}
    if tracks:
        param = 'tracks'
    else:
        param = 'artists'
    response = requests.get(url.format(param), headers=headers)
    if response.status_code != 200:
        print("get top didn't work")
        exit()
    return response.json()

def get_song(auth, songid):
    url = 'https://api.spotify.com/v1/audio-features/{}'
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json', 'Authorization': 'Bearer {}'.format(auth)}
    response = requests.get(url.format(songid), headers=headers)
    if response.status_code != 200:
        print("get song didn't work")
        exit()
    return response.json()

# take a list of album ids
def get_albums(auth, albumid):
    url = 'https://api.spotify.com/v1/albums?ids={}'
    headers = {'Accept': 'aplication/json', 'Content-Type': 'application/json', 'Authorization': 'Bearer {}'.format(auth)}
    response = requests.get(url.format('%2C'.join(albumid)), headers=headers)
    if response.status_code != 200:
        print('get albums didnt work')
        exit()
    return response.json()

# get the features of the top tracks of the user
# returns a json where 'audio_features' contains a list of features
def get_top_tracks_features(auth):
    #url = 'https://api.spotify.com/v1/audio-features?ids={}'
    url = 'https://api.spotify.com/v1/audio-features?ids=3v8FOuA8jxAC5SOA2uN6Mg'
    headers = {'Accept': 'aplication/json', 'Content-Type': 'application/json', 'Authorization': 'Bearer {}'.format(auth)}

    top = get_top(auth, True)
    processed = []
    trackids = []
    for row in top['items']:
        trackids.append(row['id'])

    response = requests.get(url.format('%2C'.join(trackids)), headers=headers)
    print(response)
    if response.status_code != 200:
        print('get top tracks features didnt work')
        exit()

    return response.json()

def get_top_artists_genres(auth):
    top = get_top(auth, False)
    process = []
    for row in top['itmes']:
        processed.append(row['genres'])
    return processed

if __name__ == '__main__':
    auth = 'BQDCe4SR_RkSsp8GlVAp1GS_qv3LMHQLC2qE9wq_KlW0Xe7SZwHL3th7gFa7eYZezdGeXXnCC_m1xTJsaa4dx1TbT61uBOvHZ2w2QqxULIUIabTz40IF_mQmn6waKUhLV6dK5qCwIX_zXwEbAs1dptGgXiwiuM3TX6yjcEGqzfQ'
    t = get_top_tracks_features(auth)
    print(t)

