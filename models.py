class Task:
    def __init__(self, name, description, priority, deadline):
        self.name = name
        self.description = description
        self.priority = priority
        self.deadline = deadline
        
    def get_info(self):
        if self.priority == 1:
            print(f'Задача: {self.name}\nОписание {self.description}\nВажность: Очень важная\nДедлайн: {self.deadline}')
        if self.priority == 2:
            print(f'Задача: {self.name}\nОписание {self.description}\nВажность: Средняя важность\nДедлайн: {self.deadline}')
        if self.priority == 3:
            print(f'Задача: {self.name}\nОписание {self.description}\nВажность: Обычная\nДедлайн: {self.deadline}')