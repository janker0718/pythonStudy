'''
#偏函数

'''


print(int('1234'))
print(int('12345', base=10)) #base代表多少进制 默认10

print(int('12345', base=16))

def int2(x, base=2):
    return int(x, base)

print( int2('1000000'))

import functools

int3 = functools.partial(int,base = 2)
print(int3('1000000'))

kw = { 'base': 2 }

print(int2('1000000',**kw))
