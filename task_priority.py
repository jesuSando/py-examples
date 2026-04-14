import datetime
import zoneinfo
import time

chile = zoneinfo.ZoneInfo("America/Santiago")

tasks = {}

def calculate_priority(deadline, difficulty):

    limit = datetime.datetime.strptime(deadline, "%Y-%m-%d %H:%M:%S").astimezone(chile)
    now = datetime.datetime.now(chile)
    
    time_left = limit - now
    seconds = round(time_left.total_seconds())
    
    priority = 0
    
    if difficulty == "hard": priority = 10
    elif difficulty == "medium": priority = 7
    else: priority = 4
    
    if seconds > 0: priority += 100000 / seconds
    else: priority += 100000
    
    return int(round(priority))
    

def task_priority(task, deadline, difficulty):

    priority = calculate_priority(deadline, difficulty)
    global tasks
    id = len(tasks) +1
    tasks[id] = {
        "task": task,
        "deadline": deadline,
        "difficulty": difficulty,
        "priority": priority
    }
    
    return tasks
    
def sort_tasks(tasks):
    for i in tasks:
        tasks[i]["priority"] = calculate_priority(tasks[i]["deadline"], tasks[i]["difficulty"])
    
    return sorted(tasks.values(), key=lambda x: x["priority"], reverse=True)


def init():
    while True:
        task = str(input("ingresa el nombre de una tarea: "))
        deadline = str(input("ingresa el tiempo limite en formato YYYY-MM-DD HH:MM:SS: "))
        difficulty = int(input("ingresa la dificultad: \n1) Dificil \n2) Media \n3) Facil \n"))
        
        if difficulty == 1: difficulty = "hard"
        elif difficulty == 2: difficulty = "medium"
        elif difficulty == 3: difficulty = "easy"
        else: print("ingresa una opcion valida")
        
        task_priority(task, deadline, difficulty)
        print("tareas ordenadas por prioridad: ")
        print(sort_tasks(tasks))
        
init()