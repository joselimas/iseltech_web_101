FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
RUN pip install Flask
COPY . /app
WORKDIR /app
ENTRYPOINT ["sh"]
CMD ["run.sh"]
