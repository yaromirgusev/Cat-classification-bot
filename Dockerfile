
FROM nvidia/cuda:12.4.1-cudnn-devel-rockylinux8

RUN apt-get update && \
    apt-get install -y \
        git \
        python3-pip \
        python3-dev \
        python3-opencv \
        libglib2.0-0

COPY requirements.txt requirements.txt

RUN python3 -m pip install -r requirements.txt

RUN pip3 install torch torchvision -f https://download.pytorch.org/whl/cu111/torch_stable.html

WORKDIR /app

ENTRYPOINT [ "python3" ]