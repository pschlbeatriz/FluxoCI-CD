FROM python:3.10

WORKDIR /app

COPY gerador_senhas.py /app/

ENTRYPOINT ["python", "gerador_senhas.py"]
