Type "help", "copyright", "credits" or "license" for more information.
>>> a={"Sham":21,"Toto":23}
>>> b={"Boom":21,"Pepe":23}
>>> print(a[1])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 1
>>> b=["Boom","Pepe"]
>>> a=["Sham"Toto"]
  File "<stdin>", line 1
    a=["Sham"Toto"]
             ^
SyntaxError: invalid syntax
>>> a=["Sham","Toto"]
>>> print(a[0])=b[0]
  File "<stdin>", line 1
SyntaxError: cannot assign to function call
>>> print(a[0])
Sham
>>> print(b[0])
Boom
>>> print(a[0])=b[1]
  File "<stdin>", line 1
SyntaxError: cannot assign to function call
>>> 
KeyboardInterrupt
>>> print(a[0])=(f'{b[0]}')
  File "<stdin>", line 1
SyntaxError: cannot assign to function call
>>> d=b[0]
>>> d
'Boom'
>>> print(a[0])=d
  File "<stdin>", line 1
SyntaxError: cannot assign to function call
>>> (a[0])=d
>>> a
['Boom', 'Toto']
>>> (a[0])=b[1]
>>> a
['Pepe', 'Toto']
>>> 

