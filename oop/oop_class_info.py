'''

    获取对象信息
'''
import types

def fn():
    pass
print(type(123) == int)

print(type("str"))

print(type(None))

print( type(abs))

print(type(fn) == types.FunctionType)

print( type(123)==type(456))

print(type(lambda x :x ) == types.LambdaType)

print(type((x for x in range(10)))== types.GeneratorType)

