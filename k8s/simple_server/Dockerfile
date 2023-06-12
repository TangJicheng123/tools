FROM ubuntu:22.04
LABEL maintainer="tangjicheng"
ENV DEBIAN_FRONTEND noninteractive

RUN apt update && \
    apt install -y wget vim git git-lfs curl && \
    apt install -y python3 python3-pip

RUN mkdir -p /app
WORKDIR /app

ADD main.py /app/main.py

ADD requirements.txt /app/requirements.txt
RUN pip3 install -r /app/requirements.txt

EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]


