import schedule
from time import sleep
import requests
from datetime import datetime




#Função que busca o preço do bitcoin
def cotacao_btc():
    resultado = requests.get('https://economia.awesomeapi.com.br/json/last/btc-brl')
    cotacao_atual = resultado.json()['BTCBRL']['ask']
    horario_atual = datetime.now().strftime('%H:%M:%S - %d/%m/%Y')
    print(f'O Bitcoin está em R${cotacao_atual} no horário {horario_atual}')

#Agendando a cada 12 horas
schedule.every(12).hours.do(cotacao_btc)

while True:
    schedule.run_pending()
    sleep(2)
