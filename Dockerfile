FROM python:3.11

RUN pip install Flask

# mount /public dir into container
RUN mkdir /app
COPY public/ /app
WORKDIR /app

# app runs on port 8080
ENV PORT 8080

# run the app
CMD python3 app.py