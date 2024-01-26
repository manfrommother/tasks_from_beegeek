class Todo():

    def __init__(self):
        self.dict_buisness = {}
        self.things = []

    def add(self, buisness, priority):
        self.dict_buisness[buisness] = priority

    def get_by_priority(self, search_priority):
        return [i for i, value in self.dict_buisness.items() if value == search_priority]
    
    def get_low_priority(self):
        if len(self.dict_buisness) == 0:
            return []
        low_priority = min(self.dict_buisness.values())
        return [i for i, value in self.dict_buisness.items() if value == low_priority]
    
    def get_high_priority(self):
        if len(self.dict_buisness) == 0:
            return []
        high_priority = max(self.dict_buisness.values())
        return [i for i, value in self.dict_buisness.items() if value == high_priority]


todo = Todo()

print(todo.things)
todo.add('Ответить на вопросы', 5)
todo.add('Сделать картинки', 1)
todo.add('Доделать задачи', 4)
todo.add('Дописать конспект', 5)
print(todo.get_by_priority(3))

print(todo.get_low_priority())
print(todo.get_high_priority())
