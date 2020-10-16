import pickle
import pandas as pd
from fastapi import FastAPI, Query
from typing import Optional

app = FastAPI(
    title="Movie recommendation API",
    description="A movie recommendation API built in Python with scikit learn models and fastapi web framework",
    version="0.0.1"
)


# Import the dataframe posprocessed
df = pd.read_csv("data/movies_pos.csv")
# Import the model trained - use pickle
y = pickle.load(open('data/cosine.pkl', 'rb'))


@app.get("/movies/")
async def search_movie(q: str = Query(..., min_length=2, max_length=40)):
    movies = df[df.original_title.str.contains(q)]
    results = [{"id": movie[0], "title": movie[1].original_title}
               for movie in movies.iterrows()]
    return results


@app.get("/movies/{movie_id}")
def read_movie(movie_id: int):
    movie = df.iloc[movie_id]
    return {"id": movie_id,
            "title": movie.original_title,
            "genres": movie.genres,
            "overview": movie.overview}


@app.get("/movies/{movie_id}/recommendation")
async def read_movie_rec(movie_id: int):
    # Get a list of similar movies in descending order of cosine similarity
    movie_similarity = pd.DataFrame({'cos_similarity': y[movie_id]}).sort_values(
        by='cos_similarity', ascending=False)
    get_50_i = movie_similarity.head(31).index
    recommendation_list = list(df.iloc[get_50_i]['original_title'].values)
    return {"movie": recommendation_list[0], "recommendation_list": recommendation_list[1:]}
