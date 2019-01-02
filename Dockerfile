FROM python:3.7-alpine3.8
RUN mkdir /code
WORKDIR /code
ADD . /code/
EXPOSE 5000
RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories
RUN apk add --no-cache build-base && apk add --no-cache mariadb-connector-c-dev
RUN pip install --no-cache-dir -r requestment.txt  -i https://pypi.douban.com/simple
RUN apk del build-base