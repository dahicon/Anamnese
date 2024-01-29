import os

inscritos_recentes = ['Rebeca', 'Rafael', 'Marcelo', 'Rede', 'Abbadon', 'Vip007', 'Tutorial']

with open('FichadeAnamnese.txt', 'w', newline='') as file:
    for line in inscritos_recentes:
        file.write(line + os.linesep)

        #faz as mesmas perguntas do "ficha.py" porém converte em um arquivo .txt