class CallMe:
    def __call__(self, *args, **kwargs):
        print('Called:', args, kwargs)


C = CallMe()
print(C(4.5, x=10, my=8))


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        rep = 'Person(' + self.name + ',' + str(self.age) + ')'
        return rep


person = Person("John", 20)
print(repr(person))


class Person:
    @staticmethod
    def is_adult(age):
        if age > 18:
            return True
        else:
            return False


print(Person.is_adult(23))


class MyClass:
    TOTAL_OBJECTS = 0

    def __init__(self):
        MyClass.TOTAL_OBJECTS = MyClass.TOTAL_OBJECTS + 1

    @classmethod
    def total_objects(cls):
        print("Total objects: ", cls.TOTAL_OBJECTS)


my_obj1 = MyClass()
my_obj2 = MyClass()
my_obj3 = MyClass()

print(MyClass.total_objects())


class MyCat:
    def __init__(self, tail_cat):
        self.tail_cat = tail_cat

    @property
    def tail(self):
        return self.tail_cat

    @tail.setter
    def tail(self, cat_tail):
        self.tail_cat = cat_tail

    @tail.deleter
    def tail(self):
        self.tail_cat = 1


m = MyCat(2)
print(f'Хвосто у кота: {m.tail}')
m.tail = 3
print(f'Хвосто у кота: {m.tail}')
del m.tail
print(f'Хвосто у кота: {m.tail}')