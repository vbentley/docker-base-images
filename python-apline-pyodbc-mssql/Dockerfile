FROM python:3.8-alpine
RUN apk update
RUN apk add curl sudo build-base unixodbc-dev unixodbc freetds-dev && pip install pyodbc
RUN apk add --no-cache tzdata
ENV TZ America/Phoenix
RUN rm -rf /var/cache/apk/*
RUN curl -O https://download.microsoft.com/download/e/4/e/e4e67866-dffd-428c-aac7-8d28ddafb39b/msodbcsql17_17.5.2.2-1_amd64.apk
RUN sudo sudo apk add --allow-untrusted msodbcsql17_17.5.2.2-1_amd64.apk