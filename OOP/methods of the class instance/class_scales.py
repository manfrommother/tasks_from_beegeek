class Scales():

    def __init__(self):
        self.right = 0
        self.left = 0

    def add_right(self, weight):
        self.right += weight

    def add_left(self, weight):
        self.left += weight

    def get_result(self):
        if self.left > self.right:
            return f'Левая чаша тяжелее'
        elif self.left < self.right:
            return f'Правая чаша тяжелее'
        else:
            return f'Весы в равновесии'


scales = Scales()

scales.add_right(1)
scales.add_left(2)

print(scales.get_result())