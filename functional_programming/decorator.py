'''

    # 装饰器 这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
    # decorator就是一个返回函数的高阶函数。
'''

def log(func):
    def wrapper(*args,**kw):
        print('call %s():' % func.__name__)
        return func(*args,**kw)
    return wrapper

@log # @log 相当于 now = log(now)
def now():
    print('2017-07-26')
now()
print(now.__name__)
def log2(text):
    def decorator(func):
        def wrapper(*args,**kw):
            print('%s %s():' %  ( text,func.__name__) )
            return func(*args,**kw)
        return wrapper
    return decorator

@log2('execute') #相当于 now = log('execute')(now)
def now2():
    print('2017-07-26')
now2()
print(now2.__name__)


import  functools
def log3(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print('%s %s():' %  ( text,func.__name__) )
            return func(*args,**kw)
        return wrapper
    return decorator
@log3('execute')
def now3():
    print('2017-07-26')
now3()

