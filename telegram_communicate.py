import requests

token = '455959783:AAEDSt7GS21RrdMaxqrqvhypRxmgDe6lUgo'
url = 'https://api.telegram.org/bot'

try:
    res = requests.post(url + token + '/getUpdates').json()
    id = res['result'][0]['message']['chat']['id']
except:
    print('Error getting updates')

send_text = 'Hello world!'
send_str = url + token + '/sendMessage?chat_id=' + str(id) + '&text=' + send_text

requests.post(send_str)
