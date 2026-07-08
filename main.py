tasks = []

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
    
menu_list()

while True:
    print("\n0. Меню")
    op = int(input("Выберите пункт: "))

    match op:
        case 0:
            menu_list()
        case 1:
            add_task()
        case 2:
            show_tasks()
        case 3:
            rename_task()
        case 4:
            pop_task()
        case 5:
            search_task()
        case 6:
            break

