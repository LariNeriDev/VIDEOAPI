#Use a imagem Python como base
FROM python:3.7

# Definir um diretório de trabalho
WORKDIR /app

# Copiar arquivos da aplicação para o diretório de trabalho
COPY . .

# Instalar dependências
RUN pip install --no-cache-dir -r requirements.txt

#Executar a aplicação quando a imagem for iniciada
CMD ["uvicorn", "app.routes.posts:app", "--host", "0.0.0.0", "--port", "8000"]