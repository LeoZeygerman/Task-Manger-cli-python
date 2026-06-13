from storage import save_data, load_data

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
            
            
    except ValueError:
        print('Ошибка при вводе!')
    