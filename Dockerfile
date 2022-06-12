FROM python:3-alpine

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src ./src

# Add non root user
RUN addgroup -S python && adduser -S python -G python
RUN chown -R python:python ./
USER python

EXPOSE 8000

CMD [ "uvicorn", "src.main:app", "--host", "0.0.0.0"]