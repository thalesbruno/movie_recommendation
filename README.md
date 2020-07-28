# Movie Recommendation

Still in development...

### Usage

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

Run the fastapi server
```python
uvicorn api:app --reload
```

Access the application on: `http://127.0.0.1:8000`   
Access the API documentation on : `http://127.0.0.1:8000/docs` or `http://127.0.0.1:8000/redoc`

Make request using a browser, the docs pages or any other API request application

Example using `curl`
```
curl -X GET "http://127.0.0.1:8000/movies/0/recommendation" -H  "accept: application/json"
```