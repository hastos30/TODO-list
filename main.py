from todoList import TodoList

def menu_list():
    print("\nTODO-list")
    print("1. Создать задачу")
    print("2. Список задач")
    print("3. Переименовать задачу")
    print("4. Удалить задачу")
    print("5. Поиск задачи")
    print("6. Выход")

todo = TodoList()
todo.load_txt('list')

while True:
    menu_list()
    try:
        op = int(input("Выберите пункт: "))
    except ValueError:
        print("Введите число")
        continue
    match op:
        case 1:
            title = input("Введите название задачи: ")
            todo.add_task(title)
            todo.save_txt('list')
            print("Задача добавлена")
        case 2:
            todo.show_tasks()
        case 3:
            if not todo.tasks:
                print("Список пуст")
                continue

            todo.show_tasks()

            try:
                task_id = int(input("Введите ID задачи: "))
            except ValueError:
                print("Введите число")
                continue

            new_title = input("Введите новое значение: ")

            if todo.rename_task(task_id, new_title):
                todo.save_txt('list')
                print("Задача переименована")
            else:
                print("Задача не найдена")
        case 4:
            todo.show_tasks()
            task_id = int(input("Введите ID задачи: "))

            if todo.remove_task(task_id):
                todo.save_txt('list')
                print("Задача удалена")
            else:
                print("Задача не найдена")
        case 5:
            text = input("Введите текст для поиска: ")
            result = todo.search_task(text)

            if result:
                print("Найденные задачи: ")
                for task in result:
                    print(task)
            else:
                print("Ничего не найдено")
        case 6:
            print("До свидания!")
            break
        case _:
            print("Некорректный пункт меню")


# Это я оставил для себя, что бы одталкиваться от того, 
# как сделать реализацию сохранения и записи 
# списка с таксками в файл

# def save_list():

#     op = int(input("В каком формате сохранить 1.TXT 2.JSON: "))
#     match op:
#         case 1:
#             with open('src/save/list.txt', 'w', encoding='utf-8') as file:
#                 for item in tasks:
#                     file.write(f"{item}\n")
#         case 2:
#             with open('src/save/list.json', 'w', encoding='utf-8') as file:
#                 json.dump(tasks, file, ensure_ascii=False, indent = 4)
#         case _:
#             print("Некоректный ввод! Попробуйте еще раз")
#             save_list()
    
#     print("Список сохранён!")

# def open_list():
#     op = int(input("Какой формат файла запустить 1.TXT 2.JSON: "))
#     match op:
#         case 1:
#             try:
#                 with open('src/save/list.txt', 'r', encoding='utf-8') as file:
#                     return [line.rstrip() for line in file]
#             except FileNotFoundError:
#                 return []
#         case 2:
#             try:
#                 with open('src/save/list.json', 'r', encoding='utf-8') as file:
#                     return json.load(file)
#             except FileNotFoundError:
#                 return []
#         case _:
#             print("Некоректный ввод! Попробуйте еще раз")
#             open_list()