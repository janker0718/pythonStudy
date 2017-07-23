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