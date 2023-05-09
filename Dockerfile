FROM python:3.10

WORKDIR /SappGPT

COPY ./requirements.txt /SappGPT/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /SappGPT/requirements.txt

COPY ./sappgpt.py /SappGPT/

COPY ./helper /SappGPT

CMD ["uvicorn", "sappgpt:app", "--host", "0.0.0.0", "--port", "8000"]