#Aprendendo a criar um relógio digital que mosre a hora exata!

import datetime

hora_atual = datetime.datetime.now()
print('A hora atual é: ' +hora_atual.strftime('%H:%M:%S') + ' horas!')

print('Para ver a hora atual, você pode olhar para o relógio aqui no programa!')