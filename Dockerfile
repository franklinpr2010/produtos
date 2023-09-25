FROM python:3.8
COPY requirements.txt /produtoapp/requirements.txt
WORKDIR /produtoapp
RUN pip install -r requirements.txt
COPY . /produtoapp
ENTRYPOINT ["python"]
CMD ["app.py"]