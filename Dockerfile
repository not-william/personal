FROM python:3.8
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
RUN python -m pip install 'git+https://github.com/facebookresearch/detectron2.git'
COPY . /code/

