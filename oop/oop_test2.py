'''

'''

class Student2(object):

    def __init__(self,name,age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
            return self.__age
    def print_age(self):
        print('%s: %s' % (self.__name, self.__age))

    def get_grade(self):
        if self.__age >= 90:
            return 'A'
        elif self.__age >= 60:
            return 'B'
        else:
            return 'C'

bart = Student2('Bart Simpson', 59)
print(bart.get_grade())
bart.age = 8
lisa = Student2('Lisa Simpson', 87)
print(bart.age)
print(lisa.get_name())

