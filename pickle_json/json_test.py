'''

json进阶

'''
import json


def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score



s = Student('Bob', 20, 88)
print(json.dumps(s, default=student2dict))
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str,object_hook=dict2student))
print(json.dumps(s, default=lambda obj: obj.__dict__))