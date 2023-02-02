# VIDEOPOSTAPI

Projeto Backend com FastAPI, MongoDB e PyMongo
Este é um projeto de exemplo de como construir uma API RESTful com FastAPI, MongoDB e PyMongo.

## Requisitos
Docker
Docker Compose
## Como executar o projeto
Clone o repositório:

$ git clone https://github.com/seu-usuario/seu-repositorio.git

## Execute o comando abaixo para subir os containers do MongoDB e FastAPI:

$ docker-compose up -d

Acesse o Swagger UI da API em http://localhost:8000/docs para ver a documentação e testar as rotas.

## Para encerrar a execução dos containers, execute:

$ docker-compose down

# Arquitetura do projeto
O projeto consiste em duas camadas: API e Banco de Dados.

## API
A API foi construída com FastAPI e utiliza o PyMongo para se conectar ao MongoDB e realizar as operações no banco.

O Swagger UI é gerado automaticamente com as rotas e descrições definidas na API.

## Banco de Dados
O banco de dados utilizado é o MongoDB e é gerenciado com o Docker Compose.