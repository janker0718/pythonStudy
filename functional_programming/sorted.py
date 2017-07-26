'''
#     排序算法

'''

a = sorted([36, 5, -12, 9, -21])

print(a)
b = sorted([36, 5, -12, 9, -21],key=abs)
print(b)

c = sorted(['bob', 'about', 'Zoo', 'Credit'])
print(c)

d = sorted(['bob', 'about', 'Zoo', 'Credit'],key=str.lower)
print(d)

e = sorted(['bob', 'about', 'Zoo', 'Credit'],key=str.lower,reverse=True)
print(e)

# test
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return t[0]

L2 = sorted(L, key=by_name)
print(L2)

def by_score(t):
    return t[1]

L3 = sorted(L, key=by_score)

print(L3)
