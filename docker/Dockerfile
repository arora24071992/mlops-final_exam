# start by pulling the python image
FROM python:3.8.15-slim-buster

RUN python3 -m pip install --upgrade pip

# copy the requirements file into the image
COPY ./requirements.txt /exp/requirements.txt

# switch working directory
WORKDIR /exp

# install the dependencies and packages in the requirements file
RUN pip3 install -r requirements.txt

# copy every content from the local file to the image
COPY ./api/app.py /exp

EXPOSE 5000

ENV FLASK_APP=app

CMD ["python3","-m", "flask","run","--host=0.0.0.0" ]