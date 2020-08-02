FROM python:3.8

WORKDIR /app
COPY . .
RUN ["pip", "install", "-r", "requirements.txt"]

EXPOSE 8000
VOLUME ["/app/data"]

RUN ["python3", "preprocess.py"]
RUN ["python3", "recommendation.py"]

ENTRYPOINT ["uvicorn", "api:app", "--host", "0.0.0.0"]
