FROM python:3.9-slim-buster

WORKDIR /app
COPY . /app

CMD ["python", "unpack_file.py"]
