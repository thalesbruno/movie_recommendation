FROM python:3.8

WORKDIR /app
COPY . .
RUN ["pip", "install", "-r", "requirements.txt"]
RUN ["python3", "preprocess.py"]
RUN ["python3", "recommendation.py"]

EXPOSE 8000
VOLUME ["/app/data"]

ENTRYPOINT ["uvicorn", "api:app", "--host", "0.0.0.0"]
