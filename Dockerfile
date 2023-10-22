FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt ./
COPY pytest.ini ./
RUN pip install --upgrade install && pip --no-cache-dir -r requirements.txt
COPY . /app