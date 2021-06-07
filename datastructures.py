List 

a=[23,25,1,123]
a.append(23)
a.insert(0,12)
a.insert(3,56)
a.remove(23)
a.sort()
print(a)

a=[12,98,67,48,97,36,27]
>>> a[0:4]
[12, 98, 67, 48]
>>> a[2:-2]
[67, 48, 97]
>>> a[0::3]
[12, 48, 27]


Add another list b in a
a=[22,14,16]
b=[1,45,67,89,93,23]
b.append(a)
print(b)
print(b[-1])
print(b)
del b[-1]
b.extend(a)
print(b)

lists as stack and queue

a=[14,45,36,67,83,98]
print(a)
a.pop()
a.pop()
a.pop()
a.append(34)
a.insert(2,56)
a.pop(0)
print(a)

Tubles

You cannot del/add/edit any value inside the tuple.

a='red','pink','green','blue'
print(a)
print(a[1])
for x in a:
    print(x,end=' ')
del a[0] #doesn't support
print(a)


divmod(17,2)
(8,1)

a='red','pink','green','blue'
print(type(a))
print(type(len))

Sets
a=set('abcdefghijkl')
b= set('adhsiemsgzx')
print(a)
print(b)
print(a&b)
print(a|b)
print(a^b)
a.add('z')
b.pop()
print(a)
print(b)

Dictionaries

data={'kushal':'fedora','kart_':'Debian','Jace':'Mac'}
data['parthan']='Ubuntu'
del data['kart_']
print(data)
print('parthan' in data)

for i, j in enumerate (['a','b','c','d']):
    print(i,j)
    
    
>>> data1 = {}
>>> data1.setdefault('name',[]).append('rupy')
>>> data1
{'name': ['rupy']}



