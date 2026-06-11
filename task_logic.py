from storage import save_data, load_data

def add_task():
    try:
        while True:
            name = input('Введите название задачи: ')
            description = input('Введите описание задачи: ')
            print('1.Важна задача')
            print('2.Задача средней важности')
            print('3.Обычная задача')
            priority = int(input('Введите номер важности задачи: '))
            deadline = ('Введите дедлайн: (ГГГГ-ММ-ДД): ')
    except ValueError:
        print('Ошибка при вводе!')
    