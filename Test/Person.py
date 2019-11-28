class Person:
    def run(self):
        print("Person is running" + str(self.name) + str(self.age))

    def __init__(self, name="holiday", age="20"):
        print("init__")
        self.name = name
        self.age = age

    def __new__(cls, *args, **kwargs):
        print("__new__")
        return object.__new__(cls)


p = Person()
p.run()
