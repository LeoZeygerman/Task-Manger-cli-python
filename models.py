from datetime import date, datetime
class Task:
    def __init__(self, name, description, priority, deadline, status):
        self.name = name
        self.description = description
        self.priority = priority
        self.deadline = deadline
        self.status = status
        
    def get_info(self):
        if self.priority == 1:
            print(f'Задача: {self.name}\nОписание {self.description}\nВажность: Очень важная\nДедлайн: {self.deadline}\nСтатус: {self.status}\n=====')
        if self.priority == 2:
            print(f'Задача: {self.name}\nОписание {self.description}\nВажность: Средняя важность\nДедлайн: {self.deadline}\nСтатус: {self.status}\n=====')
        if self.priority == 3:
            print(f'Задача: {self.name}\nОписание {self.description}\nВажность: Обычная\nДедлайн: {self.deadline}\nСтатус: {self.status}\n=====')
            
    def one_info(self):
        today = date.today()
        deadline = datetime.strptime(self.deadline, '%Y-%m-%d').date()
        if deadline > today:
            left = (deadline - today).days
            print(f'Задача: {self.name}\nОписание {self.description}\nВажность: Обычная\nСколько осталось до сдачи: {left}\nСтатус: {self.status}\n=====')
        elif deadline < today:
            print(f'Задача: {self.name}\nОписание {self.description}\nВажность: Обычная\nДедлайн уже прошел!\nСтатус: {self.status}\n=====')