# 1 
FROM python:3.11

# 2
RUN pip install Flask gunicorn

# 3
COPY server/ /app
COPY static/ /static
WORKDIR /app

# 4
ENV PORT 5000

# 5
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 app:app