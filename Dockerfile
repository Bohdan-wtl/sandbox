FROM python:3.12-slim-bookworm

WORKDIR /app/workspace

COPY ./requirements.txt /app/workspace

RUN apt-get update && \
    apt-get install -y wget xvfb default-jre && \
    python -m pip install --upgrade pip && \
    pip install -r requirements.txt && \
    wget https://github.com/allure-framework/allure2/releases/download/2.25.0/allure-2.25.0.tgz && \
    tar -zxvf allure-2.25.0.tgz -C /opt/ && \
    ln -s /opt/allure-2.25.0/bin/allure /usr/local/bin/allure && \
    chmod +x /usr/local/bin/allure

RUN python -m pip install playwright && \
    python -m playwright install --with-deps

COPY . /app/workspace
