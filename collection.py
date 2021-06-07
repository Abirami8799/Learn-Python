>>> c=Counter(a=4,b=3,c=6)
>>> list(c.elements())
['a', 'a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'c', 'c', 'c', 'c']
>>> 
>>> from collections import defaultdict
>>> s=[('yellow',1),('red',2),('pink',3)]
>>> d= defaultdict(list)
>>> for k,v in s:
...  d[k].append(v)
... 
>>> d.items()
dict_items([('yellow', [1]), ('red', [2]), ('pink', [3])])
>>> 
>>> from collections import namedtuple
>>> Point = namedtuple('Point',['x','y'])
>>> p= Point(10,y=20)
>>> p
Point(x=10, y=20)
>>> p.x+p.y
30
>>> x,y=p
>>> x
10
>>> y
20
>>> 

