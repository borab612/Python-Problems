import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.randint(1,100, 40).reshape(10, -1), columns=list('pqrs'), index=list('abcdefghij'))

# for each row, find the nearest row to that row and the min distance 

def dist(df,k): # df is a dataframe
    ind = (df.iloc[k] - df.iloc[np.delete(np.arange(len(df.index)), k)])**2
    dsts = np.sqrt(ind.sum(axis = 1)) # these are the distances between row k and all others
    mini, rmin = dsts.min(), dsts.index[dsts.argmin()]
    return np.array([rmin, mini])

arr = np.array([])

for i in range(len(df.index)):
    arr = np.append(arr, dist(df,i))

nearest = pd.DataFrame(arr.reshape((10,2)), columns = ['Nearest Row', 'Distance'], index = df.index)
print(nearest)