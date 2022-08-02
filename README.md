# Cloud Function Python

Repositório que centraliza exemplos de implementação de serviços a serem executados no modo Serverless, especificamente no Cloud Function do Google Cloud Platform.

## Projetos

Cada pasta é um projeto diferente, exemplificando cada tipo de uso do Cloud Functions:

- [helloworld](./helloworld): Um serviço que trabalha com trigger HTTP e que exibe somente uma simples frase no browser
- [blurring](./blurring): Um serviço que aplica o filtro _blur_ nas imagens enviadas ao bucket especificado do GCS. Esse upload é o trigger acionado.