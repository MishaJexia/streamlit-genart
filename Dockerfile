FROM python:3.8.0
WORKDIR /app
COPY . .
ENTRYPOINT streamlit run genart.py