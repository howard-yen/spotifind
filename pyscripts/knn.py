from sklearn.neighbors import NearestNeighbors
import numpy as np

def knn():
    X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
    nbrs = NearestNeighbors(n_neighbors=2, algorithm='ball_tree').fit(X)
    distances, indices = nbrs.kneighbors(X)
    indices

if __name__=='__main__':
    knn()
