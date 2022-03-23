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
    while True:
        print(process.status())
        
        
        seconds += 1
        if seconds > 59:
            seconds = 0
            minutes += 1
        if minutes > 59:
            hours += 1
            minutes = 0

        print(f"{hours} horas, {minutes} minutos e {seconds} segundos")

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
                print(f"Processo {processName} rodando.")
                timer(p, processIndex)    
                        
        except:
            pass






    





"""

def searchProcess(processid, processcheck):
    plist = psutil.pids()

    for i in range(0, len(plist)):
        try:
            p = psutil.Process(plist[i])
            if p.cmdline()[0].find(user_processes[processid]['name']) != -1:
                process = p 
                processcheck == True

"""