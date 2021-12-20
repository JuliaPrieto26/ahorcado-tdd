FROM python:3.9-slim-bullseye

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt
RUN pip install --upgrade pip

COPY . .
CMD ["gunicorn", "app:app" , "--workers=1", "--threads=1"]
