# start by pulling the python image
FROM python:3.8-slim

RUN apt-get update

WORKDIR /app
# copy the requirements file into the image
COPY ./requirements.txt .

# switch working directory
# install the dependencies and packages in the requirements file
RUN apt-get install -y python3-dev default-libmysqlclient-dev build-essential
RUN pip install -r requirements.txt

# copy every content from the local file to the image
COPY . /app

# configure the container to run in an executed manner
ENTRYPOINT [ "python" ]

CMD ["main.py" ]