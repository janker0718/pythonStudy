'''

# 列表生成式
'''

a = list(range(1,11))
print(a)
L = []
for x in range(1,11):
    L.append(x * x)

print(L)

print( [x * x for x in range(1, 11)])

print([m+n for m in 'ABC' for n in 'XYZ' ])

import  os #导入os模块，模块的概念后面讲到

print([d for d in os.listdir('.')]) # os.listdir可以列出文件和目录

d = {'x':'A','y':'B'}

for k,v in d.items():
    print(k,":",v)

print([k + '=' + v for k,v in d.items()])
L = ['Hello', 'World', 'IBM', 'Apple']

print([s.lower() for s in L])


