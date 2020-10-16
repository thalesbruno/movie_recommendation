from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import pickle


# Read the data set
movies = pd.read_csv("data/movies_pos.csv")

# Create a count matrix from this new combined column
# Use TFIDF to evaluate how relevant is each word to the text
tf = TfidfVectorizer()
X = tf.fit_transform(movies.features)

# Compute the cosine similarity based on the count matrix
# The cosine similarity is the best way to similarity classification on text
y = cosine_similarity(X)

# Dump the cosine similarity vectors
pickle.dump(y, open('data/cosine.pkl', 'wb'))
