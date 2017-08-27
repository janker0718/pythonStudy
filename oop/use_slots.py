'''
绑定属性

'''

class Student(object):
    __slots__ = ("name","age")

class GraduateStudent(Student):
    pass
s = Student()

s.name = "John"

s.age = 24

try:
    s.score = 99
except AttributeError as e:
    print('AttributeError:', e)

g = GraduateStudent()
g.score = 99
print('g.score =', g.score)