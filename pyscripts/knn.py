from sklearn.neighbors import NearestNeighbors
import numpy as np
import pandas as pd

def knn():
    userdata = pd.read_csv('userdata.csv')
    ids = userdata['user_id'].to_numpy()
    X = userdata.iloc[:, 4:].to_numpy()
    nbrs = NearestNeighbors(n_neighbors=len(X), algorithm='auto').fit(X)
    _, indices = nbrs.kneighbors(X)
    similarity = {}
    for i in range(indices.shape[0]):
        similarity[ids[i]] = []
        for j in range(1, indices.shape[1]):
            similarity[ids[i]].append(ids[indices[i][j]])

    return similarity
