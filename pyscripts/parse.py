import pandas as pd
import numpy as np

def read_genres():
    genres_csv = pd.read_csv('genres.csv')
    
    nums = genres_csv['number'].to_numpy()
    genre = genres_csv['genre'].to_numpy()
    
    genres_dict = dict()
    for i in nums:
        genres_dict[genre[i-1]] = i 

    return genres_dict


