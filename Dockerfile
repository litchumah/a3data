FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 
COPY ./iris.py /code/
COPY ./utils.py /code/
COPY ./pipeline.py /code/
COPY ./main.py /code/

# 
RUN python pipeline.py
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]