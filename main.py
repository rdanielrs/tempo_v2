import pathlib, json, keyboard
from tkinter import S
import filemanager
from utils import process_handler, process_monitor
from time import sleep


pid = 0
scancheck = False

mainfolder = pathlib.Path(__file__).parent.resolve()

filemanager.checkoptfile()
filemanager.checkprocess()

with open("options.json", "r") as options:
    user_options = json.load(options)

with open("user_processes.json", 'r') as processes:
    user_processes = json.load(processes)


if len(user_processes) == 0:
    process_handler.select()


while user_options['add_process'] == True:

    add_input = input('Deseja adicionar mais um processo?[s/n] ')

    if add_input.lower() == 's':
        process_handler.select()

    elif add_input.lower() == 'n':
        with open('options.json', 'w') as option:
            user_options['add_process'] = False
            json.dump(user_options, option)

        with open('user_processes.json', 'r') as processes:
            user_processes = json.load(processes)
        break;
    else:
        print("Valor não reconhecido. Insira s para sim e n para não.")
        continue;
    

    #with open('user_processes.json', 'w') as processes:
        #json.dump(user_processes, processes)




while user_options['remove_process'] == True:
    confirm_remove = input("Deseja remover um processo?[s/n] ")

    if confirm_remove.lower() == 's':
        print("=" * 50)
        for c in range(len(user_processes)):
            print(f"{c}. {user_processes[c]['name']}: {user_processes[c]['hours']} hora(s), {user_processes[c]['minutes']} minuto(s) e {user_processes[c]['seconds']} segundo(s)")
        print("=" * 50)
        
        
        remove_input = int(input("Insira o número do processo que deseja remover: "))


        if remove_input > len(user_processes) or remove_input < 0:
            print("Insira um valor válido.")
        else:
            process_handler.remove(remove_input)


    elif confirm_remove.lower() == 'n':
        with open("options.json", 'w') as options:
            user_options['remove_process'] = False
            json.dump(user_options, options)
        
        with open('user_processes.json') as processes:
            user_processes = json.load(processes)
        break;
    else:
        print("Valor inválido. Insira s para sim e n para não.")


if len(user_processes) > 0:
    print("=" * 50)
    for c in range(len(user_processes)):
        print(f"{c}. {user_processes[c]['name']}: {user_processes[c]['hours']} hora(s), {user_processes[c]['minutes']} minuto(s) e {user_processes[c]['seconds']} segundo(s)")
    print("=" * 50)

while True:
    try:
        process_monitor.searchProcess(user_processes[pid]['name'], pid)
    except:
        pass;

    pid += 1

    if pid > len(user_processes):
        pid = 0

    sleep(1)

