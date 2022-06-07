# start by pulling the python image
FROM python:3.8-slim

#RUN apt-get update

WORKDIR /app


# switch working directory
# install the dependencies and packages in the requirements file
#RUN apt-get -y install python3-dev default-libmysqlclient-dev build-essential
#RUN apt-get update && apt-get -y install apturl && pip install -r requirements.txt
RUN pip install -r requirements.txt

# copy the requirements file into the image
COPY ./requirements.txt .

# copy every content from the local file to the image
COPY . /app

# configure the container to run in an executed manner
ENTRYPOINT [ "python" ]

CMD ["app.py" ]

