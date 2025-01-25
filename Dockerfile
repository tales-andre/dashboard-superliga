# Imagem base com Python
FROM python:3.9-slim

# Definir o diretório de trabalho
WORKDIR /app

# Copiar arquivos para o contêiner
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

# Expor a porta 5000
EXPOSE 5000

# Comando para rodar a aplicação
CMD ["python", "app.py"]
