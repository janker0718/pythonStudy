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