from task_logic import add_task
def main_menu():
    while True:
        try:
            print('==TASK MANAGER==')
            print('1.Создать задачу')
            print('2.Показать все задачи')
            print('3.Найти задачу')
            print('4.Изменить задачу')
            print('5.Завершить задачу')
            print('6.Удалить задачу')
            print('7.Статистика')
            print('8.Выход')
            choice = int(input('Ваш выбор: '))
            
            if choice == 1:
                add_task()
            
        except ValueError:
            print('Ошибка при вводе!')