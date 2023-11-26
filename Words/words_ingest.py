import pandas as pd
import io
import pickle

with open('Words/words.csv') as f:
    words_raw = f.read()

csv = io.StringIO(words_raw)
df = pd.read_csv(csv, names=["Word", "Meaning"])

df.to_pickle('/Users/danross/Desktop/murmurate/Words/words.pkl')  # where to save it, usually as a .pkl

print(df)