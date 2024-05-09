FROM python:3.9-slim

WORKDIR /src

ENV PYTHONWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt .
RUN pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
RUN pip install --upgrade -r requirements.txt

COPY . .

