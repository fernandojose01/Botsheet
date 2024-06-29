# WhatsApp Bot com Google Sheets

Este projeto implementa um bot que lê dados de uma planilha do Google Sheets e envia mensagens automatizadas pelo WhatsApp usando o navegador e a biblioteca `pyautogui`.

## Requisitos

- Python 3.10
- Google API Client Library
- PyAutoGUI
- Webbrowser

## 🚀 Instalação

Para instalar o WhatsApp Bot com Google Sheets, siga estas etapas:

1. Clone este repositório:
   ```sh
   git clone https://github.com/seu-usuario/whatsapp-bot.git
   cd whatsapp-bot

2. Crie e ative um ambiente virtual (opcional, mas recomendado):
   ```sh
   python3 -m venv venv
   source venv/bin/activate  # no Windows use `venv\Scripts\activate`

3. Instale as dependências do projeto:
   ```sh
   pip install google-api-python-client pyautogui webbrowser


3. Instale as dependências do projeto:
   ```sh
   pip install google-api-python-client pyautogui webbrowser

4. Configure as credenciais do Google API:
- Acesse o Google Cloud Console.

- Crie um novo projeto ou selecione um projeto existente.

- Ative a API Google Sheets e a API Google Drive.

- Crie credenciais de OAuth 2.0 para desktop e faça o download do arquivo credentials.json.

- Coloque o arquivo credentials.json no diretório do projeto.
  

☕ Uso
Para usar WhatsApp Bot com Google Sheets, siga estas etapas:

- Prepare sua planilha no Google Sheets com as informações que deseja enviar pelo WhatsApp.

- Certifique-se de que o arquivo credentials.json está no diretório do projeto.

- Atualize o script Python com os detalhes da planilha e o formato das mensagens que deseja enviar.

- Execute o script
   ```sh
    python bot.py

5. O bot abrirá o navegador e começará a enviar as mensagens automaticamente

