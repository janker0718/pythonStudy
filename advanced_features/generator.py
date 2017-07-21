'''
#   生成器
'''


g = (x * x for x in range(10))

print(g)


print(next(g))
print(next(g))
print(next(g))
print(next(g))

r = (x * x for x in range(10))
for n in r:
    print(n)


def fib(max):
    n ,a ,b =  0, 0, 1
    while n < max:
        yield b
        a , b = b ,a+b # t = (b, a + b) # t是一个tuple     a = t[0]    b = t[1]
        n = n+1
    return 'done'
g = fib(6)
# print(f)
while True:
    try:
        x = next(g)
        print('g',x)
    except StopIteration as e:
        print('Generator return value',e.value)
        break

def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)

o = odd()
# next(o)
# next(o)

