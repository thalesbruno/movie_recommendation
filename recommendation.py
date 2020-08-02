from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import pickle


def get_index_from_title(title: str, df: pd.DataFrame) -> int:
    return df[df.title == title].index.values[0]


def get_title_from_index(index: int, df: pd.DataFrame) -> str:
    return df[df.index == index]['original_title'].values


# Read the data set
df = pd.read_csv("./data/movies_pos.csv")

# Create a count matrix from this new combined column
tf = TfidfVectorizer()
X = tf.fit_transform(df.features)

# Compute the cosine similarity based on the count matrix
y = cosine_similarity(X)

# Dump the cosine similarity vectors
pickle.dump(y, open('./data/cosine.pkl', 'wb'))
