'''
    java中的map dic
'''

map = {"name":"张三","age":33}
print(map.get("name"))

print(map["name"])
if 'name' in map:
    print(map['name'])
print(map.get('hahaha'),'hahaha')

print(map)

map.pop('age')
print(map)
