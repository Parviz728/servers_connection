class SingletonFive:
    count = 1
    def __new__(cls, *args, **kwargs):
        if cls.count <= 5:
            cls.__instance = super().__new__(cls)
            cls.count += 1
            return cls.__instance
        else:
            return cls.__instance
    def __init__(self, name):
        if not hasattr(self, "name"):
            self.name = name


objs = [SingletonFive(str(n)) for n in range(10)] # эту строчку не менять
print(objs)
for i in objs:
    print(i.name)

