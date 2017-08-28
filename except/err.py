'''
 error
'''
import logging

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():

    try:
        bar('0')
    except Exception as e:
        logging.exception(e)

main()
print('END')

class FooError(ValueError):
    pass

def foo2(s):
    n = int(s)
    if n==0:
        raise FooError('invalid value: %s' % s)
    return 10/n
foo2('0')

def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        raise

bar()

