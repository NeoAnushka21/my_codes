# start by pulling the python image
FROM python:3.8-slim

#RUN apt-get update

WORKDIR /app


# switch working directory
# install the dependencies and packages in the requirements file
COPY requirements.txt /
RUN pip install -r /requirements.txt

# copy every content from the local file to the image
COPY . /app

# configure the container to run in an executed manner
ENTRYPOINT [ "python" ]

CMD ["main.py" ]

