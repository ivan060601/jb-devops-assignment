FROM python:3.13.7-alpine

RUN pip install --no-cache-dir flask==3.1.2

WORKDIR /app
COPY app/main.py .
RUN chown -R nobody:nogroup /app

USER nobody

CMD ["python", "main.py"]