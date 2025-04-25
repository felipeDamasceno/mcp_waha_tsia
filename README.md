## Atividade: Construir um servidor MCP para envio de mensagens no WhatsApp utilizando o WAHA

### Objetivo

Você deve criar um servidor MCP que permita o envio de mensagens no WhatsApp usando o WAHA.

### Requisitos

1. **Tool: send_message**
   - O servidor deve disponibilizar uma ferramenta chamada send_message.
   - Parâmetros:
     - Número de telefone no formato internacional (ex: +5511...).
     - Mensagem a ser enviada.
   - Funcionamento:
     - A ferramenta deve se comunicar com um servidor local do WAHA.
     - Para enviar a mensagem, faça uma requisição POST para a rota `/api/sendText` do WAHA.
     - Exemplo de chamada em Python:
       ```python
       import requests

       url = "http://localhost:3000/api/sendText"
       headers = {
           "Accept": "application/json",
           "Content-Type": "application/json"
       }
       data = {
           "chatId": "123123@c.us",
           "text": "Hi there!",
           "session": "default"
       }
       response = requests.post(url, json=data, headers=headers)
       print(response.json())
       ```
     - Para rodar o servidor WAHA, siga as instruções do vídeo:  
       [YouTube: Como rodar o WAHA](https://www.youtube.com/watch?v=RFerMyAUPRg)  
       Ou consulte a documentação:  
       [WAHA Quick Start](https://waha.devlike.pro/docs/overview/quick-start/)

2. **Resource: contatos**
   - Implemente um recurso no servidor chamado contatos.
   - Este recurso deve conter pelo menos 3 contatos pré-cadastrados, cada um com nome e número de telefone.
   - Exemplo de uso: ao receber o comando "Envie uma mensagem de bom dia para o João", o servidor deve identificar o número correspondente ao nome "João" e enviar a mensagem.

### Entregáveis

- Código-fonte em um repositório (Github ou outro).
- Relatório básico de uso, incluindo prints mostrando o servidor funcionando com:
  - A ferramenta send_message.
  - O recurso contatos.

### Referências

- [WAHA Quick Start](https://waha.devlike.pro/docs/overview/quick-start/)
- [Vídeo: Como rodar o WAHA](https://www.youtube.com/watch?v=RFerMyAUPRg&ab_channel=devlikeapro)
- [Model Context Protocol - Quickstart](https://modelcontextprotocol.io/quickstart/server)