class Klass:
    _slots_ = ['a','b']
    def __init__(self):
        self.a = 1
i = Klass()
i.a

i.b = 2
i.b


class Aklass:
    def _init_(self):
        self.spam = 1
i = Aklass()
print(dir(i))