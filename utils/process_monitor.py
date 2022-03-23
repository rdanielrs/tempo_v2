from time import sleep 
import psutil, json

pid = 0

"""
O objetivo deste módulo é verificar se o processo escolhido pelo usuário se encontra em execução. 

Quando um processo selecionado é detectado, a função timer passa a contar o tempo de uso do usuário em tempo real.

"""

with open('user_processes.json', 'r') as processes:
    user_processes = json.load(processes)


def timer(process, processIndex):
    seconds = user_processes[processIndex]['seconds']
    minutes = user_processes[processIndex]['minutes']
    hours = user_processes[processIndex]['hours']

    while process.status() == 'running':
        
        seconds += 1
        if seconds > 59:
            seconds = 0
            minutes += 1
        if minutes > 59:
            hours += 1
            minutes = 0

        #print(f"{hours} horas, {minutes} minutos e {seconds} segundos")

        with open("user_processes.json", 'w') as processes:
            user_processes[processIndex]['seconds'] = seconds 
            user_processes[processIndex]['minutes'] = minutes 
            user_processes[processIndex]['hours'] = hours 
            json.dump(user_processes, processes)

        sleep(1)


def searchProcess(processName, processIndex):
    for p in psutil.process_iter():
        try:
            if processName.lower() == p.name().lower():
                print(f"Processo {processName} em execução.")
                timer(p, processIndex)  
                        
        except:
            print('Processo fechado.')
            print("=" * 50)
            for c in range(len(user_processes)):
                print(f"{c}. {user_processes[c]['name']}: {user_processes[c]['hours']} hora(s), {user_processes[c]['minutes']} minuto(s) e {user_processes[c]['seconds']} segundo(s)")
            print("=" * 50)
            pass;
