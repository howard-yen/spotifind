import numpy as np
import pandas as pd

NEARBY_THRESHOLD = 5 / 6371

def hav_dist(lat1, lon1, lat2, lon2):
    lat1, lon1, lat2, lon2 = map(np.radians, [lat1, lon1, lat2, lon2])

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    hav = np.sin(dlat/2.0)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon/2.0)**2
    angle = 2 * np.arcsin(np.sqrt(hav))
    return angle

def get_nearby():
    userdata = pd.read_csv('userdata.csv', usecols=['user_id', 'lat', 'long'])
    ids = userdata['user_id'].to_numpy()
    lats = userdata['lat'].to_numpy()
    lons = userdata['long'].to_numpy()

    dists = {}
    for i, (lat, lon) in enumerate(zip(lats, lons)):
        dists[ids[i]] = hav_dist(lat, lon, lats, lons)

    nearby_ids = {}
    for i in ids:
        nearby_ids[i] = []
        for j, d in zip(ids, dists[i]):
            if d <= NEARBY_THRESHOLD:
                nearby_ids[i].append(j)

    return nearby_ids
