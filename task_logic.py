from storage import save_data, load_data
from models import Task

def add_task():
    try:
        name = input('Введите название задачи: ')
        description = input('Введите описание задачи: ')
        print('1.Важна задача')
        print('2.Задача средней важности')
        print('3.Обычная задача')
        priority = int(input('Введите номер важности задачи: '))
        deadline = input('Введите дедлайн: (ГГГГ-ММ-ДД): ')
        print('Задача успешно создана!')
        data = load_data()
        task = {
            'name': name,
            'description': description,
            'priority': priority,
            'deadline': deadline
        }
        data.append(task)
        save_data(data)
        task_object = Task(task['name'], task['description'], task['priority'], task['deadline'])
        task_object.get_info()
            
    except ValueError:
        print('Ошибка при вводе!')
        
def show_all():
    data = load_data()
    for item in data:
        task_object = Task(item['name'], item['description'], item['priority'], item['deadline'])
        task_object.get_info()
        
def find_taks():
    data = load_data()
    find = input('Введите название задачи, которую хотите найти: ')
    for item in data:
        word = item['name']
        if find.lower() == word.lower():
            task_object = Task(item['name'], item['description'], item['priority'], item['deadline'])
            task_object.one_info()

def edit():
    try:
        while True:
            find = input('Введите название задачи, которую хотите изменить: ')
            data = load_data()
            print('1.Изменить название задачи')
            print('2.Изменить описание задачи')
            print('3.Изменить важность задачи')
            print('4.Изменить дедлайн')
            print('5.Вернуться')
            choice = int(input('Введите номер: '))
            
            if choice == 1:
                for item in data:
                    word = item['name']
                    if find.lower() == word.lower():
                        new_name = input('Введите новое название задачи: ')
                        item['name'] = new_name
                        save_data(data)
                        task_object = Task(item['name'], item['description'], item['priority'], item['deadline'])
                        task_object.one_info()
                        
            elif choice == 2:
                for item in data:
                    word = item['name']
                    if find.lower() == word.lower():
                        new_description = input('Введите новое описание задачи: ')
                        item['description'] = new_description
                        save_data(data)
                        task_object = Task(item['name'], item['description'], item['priority'], item['deadline'])
                        task_object.one_info()
            
            elif choice == 3:
                for item in data:
                    word = item['name']
                    if find.lower() == word.lower():
                        print('1.Важна задача')
                        print('2.Задача средней важности')
                        print('3.Обычная задача')
                        priority = int(input('Введите номер важности задачи: '))
                        item['priority'] = priority
                        save_data(data)
                        task_object = Task(item['name'], item['description'], item['priority'], item['deadline'])
                        task_object.one_info()
                        
            elif choice == 4:
                for item in data:
                    word = item['name']
                    if find.lower() == word.lower():
                        deadline = input('Введите новый дедлайн: (ГГГГ-ММ-ДД): ')
                        save_data(data)
                        task_object = Task(item['name'], item['description'], item['priority'], item['deadline'])
                        task_object.one_info()
            
            elif choice == 5:
                break                               
        
    except ValueError:
        print('Ошибка при вводе!')
        return
    
def delete_task():
    data = load_data()
    choice = input('Введите название задачи, которую хотите удалить: ')
    for item in data:
        word = item['name']
        if choice.lower() == word.lower():
            data.remove(item)
            save_data(data)
            print('Задача успешно удалена!')
        
