import numpy as np

NEARBY_THRESHOLD = 5 / 6371

def hav_dist(lat1, lon1, lat2, lon2):
    lat1, lon1, lat2, lon2 = map(np.radians, [lat1, lon1, lat2, lon2])

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    hav = np.sin(dlat/2.0)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon/2.0)**2
    angle = 2 * np.arcsin(np.sqrt(hav))
    return angle
