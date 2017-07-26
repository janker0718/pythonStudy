'''

# 高阶函数

'''

a = abs(-10)

print(a)
f = abs

print(f(-10))

def add(x,y,f):
    return f(x) + f(y)
x = -5
y = 6

print(add(x,y,abs))



'''
    map 
'''

def d(x):
    return x*x
r = map(d,[1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(r))


print(list(map(str,[1, 2, 3, 4, 5, 6, 7, 8, 9])))

from functools import reduce

def add(x,y):
    return  x + y
print(reduce(add,[1,3,5]))

def fn(x,y):
    return x*10 + y
print(reduce(fn,[1,3,5,7,9]))

def char2num(s):
  return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

print(reduce(fn,map(char2num,'13579')))

def str2int(s):
    return reduce(fn,map(char2num,s))

def str2int2(s):
    return reduce(lambda x,y:x*10 + y,map(char2num,s))
print('str2int2:',str2int2('13579'))

# test

def upToLow(x):
    return str(x).lower()
a = ['adam', 'LISA', 'barT']

r = map(upToLow,a)
print(list(r))