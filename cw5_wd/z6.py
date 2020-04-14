class Wspak:
    """Iterator zwracający wartości w odwróconym porządku"""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]
data = Wspak("Hello")
print(data.__iter__())
print(data.__next__())
print(data.__next__())
print(data.__next__())
print(data.__next__())
print(data.__next__())
data1 = Wspak("World")
print(data1.__iter__())
print(data1.__next__())
print(data1.__next__())
print(data1.__next__())
print(data1.__next__())
print(data1.__next__())
