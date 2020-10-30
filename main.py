from funcoes import hora, timezones_disponiveis,TimezoneValidador
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter

disponiveis = timezones_disponiveis()
opcoes_timezone = WordCompleter(disponiveis, ignore_case=True, match_middle=True)#completa a palavra, ignora maiusculas e minusculas,busca palavras no meio da frase.

timezone = prompt(f"Escolha o Timezone: ", completer = opcoes_timezone, validator=TimezoneValidador(), validate_while_typing=False)#variavel timezone recebe os parametros.

data_no_timezone = hora(timezone)
print(data_no_timezone.strftime("%d/%m/%Y %H:%M:%S"))# imprime timezone, dia, e hora.