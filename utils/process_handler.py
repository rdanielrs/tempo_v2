from tkinter import Tk
from tkinter.filedialog import askopenfilename
from pathlib import Path
import json

"""
O objetivo deste módulo é adicionar ou remover processos de acordo com o desejo do usuário. 

A função select abre uma janela de seleção do Windows para que um programa seja escolhido e monitorado no futuro. 

A função remove abre uma pequena janela de seleção no console onde um processo pode ser removido dado o seu identificador numérico.

"""

with open("user_processes.json") as processes:
    user_processes = json.load(processes)

def select():
    Tk().withdraw()
    filename = askopenfilename()

    process = {
        'name': Path(filename).stem + '.exe',
        'seconds': 0,
        'minutes': 0,
        'hours': 0
    }

    if process['name'] == '.exe':
        user_processes.pop()
        print("Nome não existente.")

    for p in user_processes:
        print(p['name'])
        if p['name'] == process['name']:
            print("Elemento já se encontra presente na lista.")
            user_processes.pop()
            return
        
    user_processes.append(process)

    with open('user_processes.json', 'w') as processes:
        json.dump(user_processes, processes)

def remove(pid):
    while True:

        confirm_input = input(f"Tem certeza de que deseja remover o processo {user_processes[pid]['name']}?[s/n] ")

        if confirm_input.lower() == 's':
            print(f"Processo {user_processes[pid]['name']} removido.")

            with open("user_processes.json", 'w') as processes:
                user_processes.pop(pid)
                json.dump(user_processes, processes)

            break;

        elif confirm_input.lower() == 'n':
            break; 

        else:
            print("Valor inválido. Insira s para sim ou n para não.")
