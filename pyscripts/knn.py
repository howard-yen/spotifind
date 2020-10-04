from sklearn.neighbors import NearestNeighbors
import numpy as np

def knn():
    userdata = pd.read_csv('userdata.csv')
    ids = df['user_id'].to_numpy()
    X = df.iloc[:, 5:].to_numpy()
    nbrs = NearestNeighbors(n_neighbors=len(X), algorithm='auto').fit(X)
    _, indices = nbrs.kneighbors(X)
    similarity = np.zeros(indices.shape, dtype='S30')
    for i in range(indices.shape[0]):
        for j in range(indices.shape[1]):
            similarity[i][j] = ids[indices[i][j]]

    return similarity 
