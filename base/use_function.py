'''
 # 定义函数
'''

def max(x , y):
    if (x > y):
        return x
    else :
        return y
def pow(x):
    return x*x

a = max(10,9)
print(a)

b = pow(3)
print(b)

def pow(x,n):
    s = 1
    while(n>0):
        n = n-1
        s = s*x
    return  s

c = pow(3,2)
print(c)

def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
d = power(5)
print(d)

def enroll(name, gender):
    print('name:', name)
    print('gender:', gender)

enroll('haha','john')

def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)
enroll('liuzhiyong','john',7)


enroll('Adam', 'M', city='Tianjin')


def add_end(L=None):
    if(L is None):
        L = []
    L.append('END')
    return  L
# print(add_end([1, 2, 3]))
print(add_end())

def face(n):
    if n == 1:
        return 1
    else:
        return n*face(n-1)

print(face(5))


def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)


def fact(n):
    return fact_iter(n,1)
print(fact(5))

# 利用递归函数移动汉诺塔:
def move(n, a, b, c):
    if n == 1:
        print('move', a, '-->', c)
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)

move(4, 'A', 'B', 'C')
