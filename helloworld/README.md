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
