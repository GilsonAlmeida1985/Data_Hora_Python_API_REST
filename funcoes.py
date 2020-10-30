import requests
from datetime import datetime
from prompt_toolkit.validation import Validator, ValidationError

timezones = []

def hora(timezone):#busca a hora no world time api em formato json.
    url = "http://worldtimeapi.org/api/timezone/" + timezone

    resposta = requests.get(url)

    hora = datetime.fromisoformat(resposta.json()["datetime"])

    return hora

def timezones_disponiveis():#disponibiliza lista de locais na timezone para escolha do usuario.
    global timezones

    if (len(timezones) > 0):
        return timezones

    url = "http://worldtimeapi.org/api/timezone"
    resposta = requests.get(url)
    timezones = resposta.json()

    return timezones

class TimezoneValidador(Validator):#verificador do que o usuario digitou na busca.
    def validate(self, document):
        texto = document.text

        if texto not in timezones_disponiveis():
            raise ValidationError(message="Timezone não diponível: " + texto)#gera o erro de validação.