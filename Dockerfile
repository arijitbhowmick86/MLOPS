from python:3.9-slim-buster

WORKDIR /flash-docker

RUN python3 -m pip install --upgrade pip

COPY requirements.txt requirements.txt
    
RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]

