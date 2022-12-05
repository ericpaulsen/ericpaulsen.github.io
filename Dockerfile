# 1 
FROM python:3.11

# 2
RUN pip install Flask

# 3
RUN mkdir /app
COPY app.py /app
COPY static/ /app/static
WORKDIR /app

# 4
ENV PORT 8080

# 5
CMD python3 app.py