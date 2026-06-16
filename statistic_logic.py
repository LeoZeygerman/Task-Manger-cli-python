from storage import save_data, load_data
from models import Task

def statistic():
    data = load_data()
    count = 0
    count_comp = 0
    for item in data:
        count += 1
    for comp in data:
        if comp['status'] == 'Завершено':
            count_comp += 1
    statistc = count_comp / count * 100
    print(f'Всего задач: {count}\nВыполнено задач: {count_comp}\nСтатистика выполнения: {statistc}%')