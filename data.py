import pandas as pd

# we want a function that reads the csv and cleans the data
df = pd.read_csv('res/lyrics.csv', delimiter=',')
#df1 = pd.read_csv('res/lyrics1.csv', delimiter=',')
#df2 = pd.read_csv('res/lyrics2.csv', delimiter=',')
#df3 = pd.read_csv('res/lyrics3.csv', delimiter=',')
#df4 = pd.read_csv('res/lyrics4.csv', delimiter=',')
#frames = [df1, df2, df3, df4]
#df = pd.concat(frames)

# we want a function that provides the data to the algo.py when requested
