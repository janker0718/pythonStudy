d = {'a': 1, 'b': 2, 'c': 3}

for key in d.values():
    print(key)

from collections import Iterable

print(isinstance('abc',Iterable))

print(isinstance([1,2,3], Iterable))
print(isinstance(123,Iterable))
#Python内置的enumerate函数可以把一个list变成索引-元素对
for i , value in enumerate(['A','B']):
    print(i,value)

for x,y in [(0,1),(2,3),(3,9)]:
    print(x,y)
