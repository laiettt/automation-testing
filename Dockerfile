FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt ./
COPY pytest.ini ./
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt
COPY . /app
CMD pytest