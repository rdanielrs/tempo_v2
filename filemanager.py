import os, pathlib, json

#mainfolder = pathlib.Path(__file__).parent.resolve()

"""
O objetivo deste módulo é verificar a integridade dos arquivos do programa e fazer reparos em caso de defeito ou inexistência. 

A função checkoptfile se trata do arquivo options.json, enquanto a função checkprocess se trata do arquivo user_processes.json.

"""

def checkoptfile():
    try:
        with open("options.json", 'r') as options:
            user_options = json.load(options)


            if type(user_options['add_process']) != bool:
                print("Erro no atributo add_process")

            if type(user_options['remove_process']) != bool:
                print("Erro no atributo remove_process")
            
    except:
        default_options = {
            "add_process": False,
            "remove_process": False
        }

        #os.path.join(mainfolder, "options.json")

        with open("options.json", "w") as options:
            json.dump(default_options, options)
    finally:
        print("Verificação de arquivo concluída.")


def checkprocess():
    try: 
        with open("user_processes.json") as processes:
            json.load(processes)
    except: 
        process_list = []

        #os.path.join(mainfolder, "user_processes.json")

        with open("user_processes.json", "w") as processes:
            json.dump(process_list, processes)
    finally: 
        print("Processos do usuário se encontram válidos.")
    

