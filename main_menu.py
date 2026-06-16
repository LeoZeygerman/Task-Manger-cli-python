from task_logic import add_task, show_all, find_taks, edit, delete_task
def main_menu():
    while True:
        try:
            print('==TASK MANAGER==')
            print('1.Создать задачу')
            print('2.Показать все задачи')
            print('3.Найти задачу')
            print('4.Изменить задачу')
            print('5.Удалить задачу')
            print('6.Статистика')
            print('7.Выход')
            choice = int(input('Ваш выбор: '))
            
            if choice == 1:
                add_task()
                
            elif choice == 2:
                show_all()
            
            elif choice == 3:
                find_taks()
                
            elif choice == 4:
                edit()
                
            elif choice == 5:
                delete_task()
        except ValueError:
            print('Ошибка при вводе!')