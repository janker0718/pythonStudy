'''
序列化
'''
import json
import pickle

f = open('dump.txt', 'wb')
d = dict( name = 'Bob', age = 20 ,score = 88)

print(pickle.dumps(d))

pickle.dump(d,f)

f = open('dump.txt', 'rb')

d = pickle.load(f)
f.close()

print(d)


d = dict(name='Bob', age=20, score=88)

print(json.dumps(d))
json_str = '{"name": "Bob", "age": 20, "score": 88}'

print(json.loads(json_str))

