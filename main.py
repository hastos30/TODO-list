import json

def add_task():
    new_task = input("Введите задачу: ")
    tasks.append(new_task)
    print(f"Задача добавлена")

def show_tasks():
    if not tasks:
        print("Задач нет")
    else:
        for index, task in enumerate(tasks):
            print(index, task)

def rename_task():
    show_tasks()
    new_index = int(input("Введите № индекса для изменения: "))
    new_name = input("Изменение задачи: ")
    tasks[new_index] = new_name

def pop_task():
    show_tasks()
    index = int(input("Введите № индекса для удаления: "))
    task = tasks.pop(index)
    print(f"Задача {task} - удалена")

def search_task():
    text = input("Поиск по тексту: ")

    found = False

    for index, task in enumerate(tasks):
        if text.lower() in task.lower():
            print(f"{index}. {task}")
            found = True
    
    if not found:
        print("Ничего не найдено")

def menu_list():
    print("DOTO-list\n")
    print("1. Создать задачу")
    print("2. Список задач")
    print("3. Изменить задачу")
    print("4. Удалить задачу")
    print("5. Поиск задачи")
    print("6. Выход")

def save_list():

    op = int(input("В каком формате сохранить 1.TXT 2.JSON: "))
    match op:
        case 1:
            with open('src/save/list.txt', 'w', encoding='utf-8') as file:
                for item in tasks:
                    file.write(f"{item}\n")
        case 2:
            with open('src/save/list.json', 'w', encoding='utf-8') as file:
                json.dump(tasks, file, ensure_ascii=False, indent = 4)
        case _:
            print("Некоректный ввод! Попробуйте еще раз")
            save_list()
    
    print("Список сохранён!")

def open_list():
    op = int(input("Какой формат файла запустить 1.TXT 2.JSON: "))
    match op:
        case 1:
            try:
                with open('src/save/list.txt', 'r', encoding='utf-8') as file:
                    return [line.rstrip() for line in file]
            except FileNotFoundError:
                return []
        case 2:
            try:
                with open('src/save/list.json', 'r', encoding='utf-8') as file:
                    return json.load(file)
            except FileNotFoundError:
                return []
        case _:
            print("Некоректный ввод! Попробуйте еще раз")
            open_list()

    

tasks = open_list()
menu_list()

while True:
    print("\n0. Меню")
    op = int(input("Выберите пункт: "))

    match op:
        case 0:
            menu_list()
        case 1:
            add_task()
            save_list()
        case 2:
            show_tasks()
        case 3:
            rename_task()
            save_list()
        case 4:
            pop_task()
            save_list()
        case 5:
            search_task()
        case 6:
            break

