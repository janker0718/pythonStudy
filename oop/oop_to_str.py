'''

定制类 __str__
'''

class Student(object):
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return  'Student object (name: %s)' % self.name

    def __getattr__(self, attr):
        if attr == 'score':
            return lambda :25

    def __call__(self):
        print('My name is %s.' % self.name)
    # __repr__ = __str__
s = Student('John1')
print(Student('John'))
print(s.score())
s1 = Student('Michael')
s1()
class Fib(object):
    def __init__(self):
        self.a ,self.b = 0,1

    def __iter__(self):
        return self
    def __next__(self):
        self.a , self.b = self.b,self.a +self.b
        if self.a > 100000:
         raise StopIteration
        return self.a

    def __getitem__(self, n):
        if isinstance(n, int):  # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):  # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L
for n in Fib():
    print(n)

f = Fib()
print(f[0])
print(f[:10])
print(list(range(100))[5:10])


class Chain(object):
    def __init__(self,path = ''):
        self.__path = path
    def __getattr__(self, path):
        return Chain('%s/%s' %(self.__path,path))
    def __str__(self):
        return self.__path

    __repr = __str__

    def __call__(self):
        print('My name is %s.' % self.name)
print(Chain().status.user.timeline.list)

# print(Chain().status.users('michael').repos)


