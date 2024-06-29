#Ler planilha e guardar informações sobre o nome, telefone e data de nascimento
#Criar botões personalisados no whatsapp e enviar as informações para cada cliente
#Usar os dados da planilha

from __future__ import print_function
import os.path
from urllib.parse import quote
import webbrowser
from time import sleep
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import pyautogui

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = "1E_Y7ItgCql74qE4b3BcJe8IKiVQvCGUm8g8BUKd3y-8"
SAMPLE_RANGE_NAME = "Página1!A1:C9"

def main():
    creds = None

    # Caminho completo para o arquivo credentials.json
    credentials_path = 'c:/Users/phoqu/Desktop/Python/Whatsapp/credentials.json'
    token_path = 'c:/Users/phoqu/Desktop/Python/Whatsapp/token.json'

    if os.path.exists(token_path):
        creds = Credentials.from_authorized_user_file(token_path, SCOPES)
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(credentials_path, SCOPES)
            creds = flow.run_local_server(port=0)
        with open(token_path, "w") as token:
            token.write(creds.to_json())

    try:
        service = build('sheets', 'v4', credentials=creds)

        # Call the Sheets API
        sheet = service.spreadsheets() #vou usar o google sheet

        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range=SAMPLE_RANGE_NAME).execute() #sempre que você quiser ler uma informação e editar
        values = result.get('values', [])

        if not values:
          print('No data found.')
        else:
        # Pegando a primeira linha (cabeçalhos)
         headers = values[0]
         print(f"Cabeçalhos: {headers}")

        # Acessando a primeira linha de dados
         data_row = values[1]
        
        # Pegando as informações das três primeiras colunas
         mes = data_row[0]
         telefone = data_row[1]
         valor = data_row[2]

         print(f"Mês: {mes}")
         print(f"Telefone: {telefone}")
         print(f"Valor: {valor}")

         mensagem = f'Olá Rita seu boleto do mês de {mes} é de {valor}. Baixe seu boleto no link https://www.link_do_pagamento.com.'

         link_mensagem_whatsapp = f'https://web.whatsapp.com/send?phone={telefone}&text={quote(mensagem)}'
         webbrowser.open(link_mensagem_whatsapp)
         sleep(10)
         seta = pyautogui.locateCenterOnScreen('Seta.png')
         sleep(5)
         pyautogui.click(seta[0],seta[1])
         sleep(5)
         pyautogui.hotkey('ctrl','w')
         sleep(5)

    except HttpError as err:
        print(err)

if __name__ == "__main__":
    main()