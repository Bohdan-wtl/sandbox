FROM mcr.microsoft.com/playwright/python:v1.47.0-noble
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y xvfb
COPY . .
RUN python -m playwright install
CMD ["xvfb-run", "pytest", "tests/"]
