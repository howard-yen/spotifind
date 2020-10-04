import requests

def get_top(auth, tracks=True, limit=10):
    url = 'https://api.spotify.com/v1/me/top/{}?limit={limit}'
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json', 'Authorization': 'Bearer {}'.format(auth)}
    if tracks:
        param = 'tracks'
    else:
        param = 'artists'
    response = requests.get(url.format(param, limit=limit), headers=headers)
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
    response = requests.get(url.format('%2C'.join(albumid)))
    if response.status_code != 200:
        print('get albums didnt work')
        exit()
    return response.json()

# get the features of the top tracks of the user
# returns a json where 'audio_features' contains a list of features
def get_top_tracks_features(auth):
    url = 'https://api.spotify.com/v1/audio-features?ids={}'
    headers = {'Accept': 'aplication/json', 'Content-Type': 'application/json', 'Authorization': 'Bearer {}'.format(auth)}

    top = get_top(auth, True)
    processed = []
    trackids = []
    for row in top['items']:
        trackids.append(row['id'])

    response = requests.get(url.format('%2C'.join(trackids)), headers = headers)
    if response.status_code != 200:
        print('get top tracks features didnt work')
        exit()

    return response.json()

# get a user's top artists and then get their genres
def get_top_artists_genres(auth):
    top = get_top(auth, False)
    processed = []
    for row in top['items']:
        processed.append(row['genres'])
    return processed

# get the images of the top track for each user
# return a list of userids, images, and track name
def get_neighbors_tracks(usertokens, userids):
    result = {'items': []}
    for auth, user in zip(usertokens, userids):
        top = get_top(auth, True, 1)
        track = top['items'][0]['album']
        temp = {}
        temp['userid'] = user
        temp['image'] = track['images'][0]
        temp['albumname'] = track['name']
        temp['url'] = track['external_url']
        result['items'].append(temp)
    return result


if __name__ == '__main__':
    auth = 'BQChi-zWJcd4DBwhS8yUhi2DYf-TkTqnuj52dAaLaEX9Kk5a0XifTU1t_zo9Ynh2TeUURRCv8d2GN1D0gf1tlodWAgfzHlrM1zddbM_9sUbe97o9kIMc9C65sg25vBN92lSDa5ej05GhFrU-BbkJCiskon0YRG5OQApfx_VizOd5EEX56zEQITfesy0T2QOUGvLTJBfesTCo0ErjDpjCmV7gqAtgkaMjz910VA5A6xT7lCN0PeXTAJRZ80MFLVzj_VbuPBi3lcRc'
    t = get_top_artists_genres(auth)
    print(t)

