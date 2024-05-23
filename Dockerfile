FROM --platform=$BUILDPLATFORM python:3.9-alpine AS builder

WORKDIR /app

COPY requirements.txt /app
RUN --mount=type=cache,target=/root/.cache/pip \
    pip3 install -r requirements.txt

COPY emailService ./emailService

ENTRYPOINT ["python3"]
CMD ["emailService/index.py"]