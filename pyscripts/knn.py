from sklearn.neighbors import NearestNeighbors
import numpy as np

def knn(X):
    X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
    nbrs = NearestNeighbors(n_neighbors=6, algorithm='auto').fit(X)
    distances, indices = nbrs.kneighbors(X)
    return indices
