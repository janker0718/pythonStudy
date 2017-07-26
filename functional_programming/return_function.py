'''

 # 返回函数
'''

def sum(*args):
    ax = 0
    for x in args:
        ax = ax + x
    return  ax
def lazy_sum(*args):
    def sum():
        ax = 0
        for x in args:
            ax = ax + x
        return ax
    return sum
f = lazy_sum(1,3,5,7,9)
print(f)
print(f())

def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

def count2():
    def f(j):
        def g():
            return j * j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i))
    return fs

f1 ,f2, f3 = count2()
# print(f1())
# f4 = count2()
print(f1())
print(f2())
print(f3())
# 返回闭包时牢记的一点就是：返回函数不要引用任何循环变量，或者后续会发生变化的变量。

