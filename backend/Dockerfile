# Dockerfile
FROM python:3.8

WORKDIR /app

# 安装系统依赖
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    libc-dev \
    libffi-dev \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# EXPOSE 8000

# 运行 uWSGI 服务器
CMD ["uwsgi", "--ini", "uwsgi.ini"]