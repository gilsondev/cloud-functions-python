# PubSub

Esse projeto mostra na prática como uma função é invocada quando o trigger configurado é a partir do momento que uma mensagem
é enviado para um tópico no [PubSub](https://cloud.google.com/pubsub?hl=pt-br). 

Como exemplo iremos simular uma ação de alarme, caso a mensagem contenha a palavra `ALARME`. Caso contrário, ele irá avisar
que a ação deve ser ignorada.

## Configuração do ambiente

1. Crie um ambiente virtual e instale as dependências:

```bash
$ poetry shell
$ poetry install
```

## Comandos para desenvolvimento

- Executar os testes automatizado: `make test`
- Atualizar o arquivo `requirements.txt`: `make requirements`

### Arquivo `requirements.txt`

Esse arquivo é necessário para o Cloud Functions reconhecer as dependências do projeto, com isso Poetry vai gerar esse arquivo da forma que precisa para o deploy.

## Deploy da aplicação

Para que possa efetuar o envio do _codebase_ para o Cloud Functions, é necessário seguir alguns passos:

- Possuir um projeto habilitado no GCP
- [Ativar as APIs](https://cloud.google.com/functions/quickstart&_ga=2.59100077.188439082.1658754150-2100695172.1658149097) do recurso do Cloud Functions e Google PubSub
- Criar um novo tópico
- Instalar e inicializar o [Google Cloud Platform SDK](https://cloud.google.com/sdk/docs)
- Executar o comando `make deploy`


## PubSub

### Criando tópico

Utilize o `gcloud` para executar essa ação:

```bash
gcloud pubsub topics create topic_pubsublab
```

### Publicando tópico

Para testar a execução da função no Cloud Functions, publique uma mensagem ao tópico criado:

```bash
gcloud pubsub topics publish topic_pubsublab --message "ALARM"
```