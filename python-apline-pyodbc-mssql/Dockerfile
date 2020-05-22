FROM python:3.8-alpine
RUN apk update
RUN apk add curl sudo build-base unixodbc-dev unixodbc freetds-dev && pip install pyodbc
RUN apk add --no-cache tzdata
ENV TZ America/Phoenix
RUN rm -rf /var/cache/apk/*