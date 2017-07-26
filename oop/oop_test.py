'''

'''

class Student(object):

    def __init__(self,name,age):
        self.name = name
        self.age = age
    def print_age(self):
        print('%s: %s' %(self.name,self.age))

    def get_grade(self):
        if self.age >= 90:
            return 'A'
        elif self.age >= 60:
            return 'B'
        else:
            return 'C'