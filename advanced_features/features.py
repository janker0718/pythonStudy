'''
 # 高级特性
'''

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print( [L[0], L[1], L[2]])
print(L[0:3])

r = []
n = 3
for i in range(n):
    r.append(L[i])
print(r)


L = list(range(100))
print(L)

print(L[:10])
print(L[-10:])

print(L[10:20])

print(L[::5])

e = 'abcde'[::3]

print(e)