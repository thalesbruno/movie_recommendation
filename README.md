# Movie Recommendation

### Install

#### With docker-compose

Since you already have Docker and docker-compose installed, there's just one step:

```
docker-compose up -d
```

#### With python virtual environment

Activate python virtual envirnonment and install the requirements

```python
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Preprocess the data set, actually we just clean the missing values data and create a column with the features we will use

```python
(venv) python preprocess.py
```

Create the model 
```python
(venv) python recommendation.py
```

The two previous steps we run once. The results are the data set preprocessed `movies_pos.csv` and the pickle binary `cosine.pkl` with the cosine simirality array already trained on the dataset, we will use both in the `api.py`. We only will need to run these two steps again if we change the data set, or change the preprocess steps, or the model parameters.

Run the fastapi server
```python
uvicorn api:app --reload
```

## Usage

Access the application on: `http://127.0.0.1:8000`   

Access the API documentation on : `http://127.0.0.1:8000/docs` or `http://127.0.0.1:8000/redoc`

Make request using a browser, the docs pages or any other API request application

Examples using `curl`:

#### Search for the Interstellar movie
```
curl -X GET "http://127.0.0.1:8000/movies/?q=Interstellar" -H  "accept: application/json"
```

#### Get the details of Interstellar by its ID
```
curl -X GET "http://127.0.0.1:8000/movies/93" -H  "accept: application/json"
```

#### Get a list of Interstellar similar movies
```
curl -X GET "http://127.0.0.1:8000/movies/93/recommendation" -H  "accept: application/json"
```
