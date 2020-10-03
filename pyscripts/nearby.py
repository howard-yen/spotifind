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

def get_nearby(lat, lon):
    userdata = pd.read_csv('userdata.csv', usecols=['user_id', 'latitude', 'longitude'])
    ids = userdata['user_id'].to_numpy()
    lats = userdata['latitude'].to_numpy()
    lons = userdata['longitude'].to_numpy()

    dists = hav_dist(lat, lon, lats, lons)

    nearby_ids = []
    for i, d in zip(ids, dists):
        if d <= NEARBY_THRESHOLD:
            nearby_ids.append(i)

    return np.array(nearby_ids)
