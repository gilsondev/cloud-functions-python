# Hello World

Esse projeto somente exibe na tela uma mensagem de Hello World, e que é invocado através do trigger HTTP.

## Configuração do ambiente

1. Crie um ambiente virtual e instale as dependências:

```bash
$ poetry shell
$ poetry install
```

## Comandos para desenvolvimento

- Inicializar servidor de desenvolvimento: `make serve`
- Executar os testes automatizado: `make test`
- Atualizar o arquivo `requirements.txt`: `make requirements`

### Arquivo `requirements.txt`

Esse arquivo é necessário para o Cloud Functions reconhecer as dependências do projeto, com isso Poetry vai gerar esse arquivo da forma que precisa para o deploy.

## Deploy da aplicação

Para que possa efetuar o envio do _codebase_ para o Cloud Functions, é necessário seguir alguns passos:

- Possuir um projeto habilitado no GCP
- [Ativar as APIs](https://cloud.google.com/functions/quickstart&_ga=2.59100077.188439082.1658754150-2100695172.1658149097) do recurso do Cloud Functions
- Instalar e inicializar o [Google Cloud Platform SDK](https://cloud.google.com/sdk/docs)
- Executar o comando `make deploy`
