import random


class MyList(list):
    def choice(self):
        return random.choice(self)


l = MyList([1, 3, 2, 6])
print(l)
print(len(l))
l.append(5)
print(l)
print(l.choice())
