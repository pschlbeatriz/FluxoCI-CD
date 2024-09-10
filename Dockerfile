FROM python:3.11-slim

WORKDIR /app

COPY gerador_senhas.py .

# Comando para executar o script
CMD ["python", "gerador_senhas.py"]
