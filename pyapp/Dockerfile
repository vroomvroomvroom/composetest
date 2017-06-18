FROM python:3.4-alpine
MAINTAINER https://github.com/vroomvroomvroom
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
