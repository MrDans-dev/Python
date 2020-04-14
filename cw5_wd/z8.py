class iter:
    def __init__(self, data):
        self.data = data
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.data):
            raise StopIteration
        self.index = self.index + 1
        list={'a','e','o','u','i','y'}
        for i in list:
            if self.data[self.index] in list:
                return self.data[self.index]

ob = iter("Hello")
print(ob.__iter__())
print(ob.__next__())
print(ob.__next__())
print(ob.__next__())
print(ob.__next__())
print(ob.__next__())


