'''

'''

class BoundedRepeater:

    def __init__(self, obj, times):
        self.obj = obj
        self.times = times
        self.counter = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.counter != self.times:
            self.counter += 1
            return self.obj
        else:
            raise StopIteration
        

geek = BoundedRepeater('geek', 3)

print(next(geek))
print(next(geek))
print(next(geek))

try:
    print(next(geek))
except StopIteration:
    print('Error')


print(next(geek))

