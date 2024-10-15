# Use a imagem oficial do Python
FROM python:3.10

# Desabilita o buffer de saída do Python para obter logs em tempo real
ENV PYTHONUNBUFFERED=1

# Define o diretório de trabalho dentro do contêiner
WORKDIR /code

# Copia o arquivo de dependências para o contêiner
COPY requirements.txt .

# Instala as dependências diretamente no contêiner (sem venv)
RUN pip install -r requirements.txt

# Copia todo o restante do código para o contêiner
COPY . .

# Expõe a porta 8000 (usada pelo Django)
EXPOSE 8000

# Comando para iniciar o servidor Django
CMD ["python3", "manage.py", "runserver"]
