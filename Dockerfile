FROM python:3.8

WORKDIR .
COPY . . 

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["server.py"]


