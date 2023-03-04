FROM python:3.10 AS BUILDER

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir --upgrade -r requirements.txt

FROM python:3.10-slim-buster AS IMAGE
COPY --from=BUILDER /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
WORKDIR /app

COPY ./src/ /app

CMD /opt/venv/bin/uvicorn app.main:app --host 0.0.0.0 --port 8080 --root-path="${PREFIX_API}"