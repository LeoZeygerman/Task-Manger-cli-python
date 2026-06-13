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
        for item in data:
            task_object = Task(item['name'], item['description'], item['priority'], item['deadline'])
            task_object.get_info()
            
    except ValueError:
        print('Ошибка при вводе!')
    