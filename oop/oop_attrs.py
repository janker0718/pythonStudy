'''


对象的属性
'''


class Student(object):
    str = 'Student'


    # def __init__(self,name):
    #     self.name = name

# s = Student('Bob')
# s.score = 90

# a = Student()
print(Student.str)

s = Student()
s.str = 'Michael'
del s.str

print(s.str)

