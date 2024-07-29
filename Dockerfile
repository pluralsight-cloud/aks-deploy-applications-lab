FROM python:3.8-slim-buster

WORKDIR /

RUN pip3 install Flask

COPY app.py .
COPY index.html templates/index.html

CMD ["python3", "app.py"]