import pickle
import pandas as pd
from fastapi import FastAPI

app = FastAPI()


# Import the dataframe posprocessed
df = pd.read_csv("movies_pos.csv")
# Import the model trained - use pickle
y = pickle.load(open('cosine.pkl', 'rb'))


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/movies/{movie_id}")
def read_movie(movie_id: int):
    return {"movie_id": movie_id}


@app.get("/movies/{movie_id}/recommendation")
async def read_movie_rec(movie_id: int):
    # Get a list of similar movies in descending order of cosine similarity
    movie_similarity = pd.DataFrame({'cos_similarity': y[movie_id]}).sort_values(
        by='cos_similarity', ascending=False)
    get_50_i = movie_similarity.head(51).index
    recommendation_list = list(df.iloc[get_50_i]['original_title'].values)
    return {"movie": recommendation_list[0], "recommendation_list": recommendation_list[1:]}
