FROM ubuntu:latest

LABEL key="ashishjangra"

# Set up the environment with python3
RUN apt-get -y update && apt-get install -y --no-install-recommends \
         wget \
         python3 \
         nginx \
        python3-pip \
        software-properties-common \
        ca-certificates \
    && rm -rf /var/lib/apt/lists/* && \
    pip3 install numpy \
        tensorflow==2.9.1 scikit-image \
        datetime nltk xlrd flask gevent gunicorn boto3 Pillow PyYAML cloudwatch && \
            rm -rf /root/.cache\

ENV PYTHONUNBUFFERED=TRUE
ENV PYTHONDONTWRITEBYTECODE=TRUE
ENV PATH="/opt/program:${PATH}"

# Set up the program in the image
COPY Program /opt/program
RUN chmod +x /opt/program/serve
WORKDIR /opt/program
