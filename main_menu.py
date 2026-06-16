from task_logic import add_task, show_all, find_taks, edit, delete_task, complete
from statistic_logic import statistic
def main_menu():
    while True:
        try:
            print('==TASK MANAGER==')
            print('1.Создать задачу')
            print('2.Показать все задачи')
            print('3.Найти задачу')
            print('4.Изменить задачу')
            print('5.Отметить выполнение задачи')
            print('6.Удалить задачу')
            print('7.Статистика')
            print('8.Выход')
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
                complete()
                
            elif choice == 6:
                delete_task()
                
            elif choice == 7:
                statistic()
                
            elif choice == 8:
                break
        except ValueError:
            print('Ошибка при вводе!')