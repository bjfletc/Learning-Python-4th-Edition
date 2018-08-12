'''
We’ll study object-oriented programming in Python—an optional but powerful feature
of the language that cuts development time by supporting programming by customization—
in depth later in this book. In abstract terms, though, classes define new types
of objects that extend the core set, so they merit a passing glance here. Say, for example,
that you wish to have a type of object that models employees. Although there is no such
specific core type in Python, the following user-defined class might fit the bill:
'''

class Worker:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)
