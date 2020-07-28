# d = dict('a'=22, 'b'=33, 'c'=44, 'd'=55)
# d.clear()


# d = dict('a'=22, 'b'=33, 'c'=44, 'd'=55)
# d.clear()


# PS C:\Users\qjawadwa> python.exe
# Python 3.7.5 (tags/v3.7.5:5c02a39a0b, Oct 15 2019, 00:11:34) [MSC v.1916 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>>
# >>>
# >>>
# >>> d = dict('a'=22, 'b'=33, 'c'=44, 'd'=55)
#   File "<stdin>", line 1
# SyntaxError: keyword can't be an expression
# >>> d = dict(a=22, b=33, c=44, d=55)
# >>> d
# {'a': 22, 'b': 33, 'c': 44, 'd': 55}
# >>> d['a]
#   File "<stdin>", line 1
#     d['a]
#         ^
# SyntaxError: EOL while scanning string literal
# >>> d['a']
# 22
# >>> d['b']
# 33
# >>> d.clear()
# >>> d
# {}
# >>> d['a']
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# KeyError: 'a'
# >>>
# >>>
# >>>
# >>>
# >>> d = dict(a=22, b=33, c=44, d=55)
# >>> d
# {'a': 22, 'b': 33, 'c': 44, 'd': 55}
# >>> c = d
# >>> c
# {'a': 22, 'b': 33, 'c': 44, 'd': 55}
# >>> d
# {'a': 22, 'b': 33, 'c': 44, 'd': 55}
# >>> c['a'] = 23
# >>> c
# {'a': 23, 'b': 33, 'c': 44, 'd': 55}
# >>> d
# {'a': 23, 'b': 33, 'c': 44, 'd': 55}
# >>>
# >>>
# >>>
# >>> e = d
# >>> f = c
# >>> c['b']=100
# >>>
# >>> c
# {'a': 23, 'b': 100, 'c': 44, 'd': 55}
# >>> d
# {'a': 23, 'b': 100, 'c': 44, 'd': 55}
# >>> e
# {'a': 23, 'b': 100, 'c': 44, 'd': 55}
# >>> f
# {'a': 23, 'b': 100, 'c': 44, 'd': 55}
# >>>
# >>>
# >>>
# >>> d
# {'a': 23, 'b': 100, 'c': 44, 'd': 55}
# >>> a = d.copy()
# >>> a
# {'a': 23, 'b': 100, 'c': 44, 'd': 55}
# >>> a['d'] = 1001
# >>> a
# {'a': 23, 'b': 100, 'c': 44, 'd': 1001}
# >>> d
# {'a': 23, 'b': 100, 'c': 44, 'd': 55}
# >>>
# >>>
# >>>
# >>> d
# {'a': 23, 'b': 100, 'c': 44, 'd': 55}
# >>>
# >>>
# >>>
# >>>
# >>>
# >>>
# >>>
# >>> a
# {'a': 23, 'b': 100, 'c': 44, 'd': 1001}
# >>>
# >>>
# >>>
# >>> {}.fromkeys('a','b')
# {'a': 'b'}
# >>> d = {}.fromkeys('a','b')
# >>> d
# {'a': 'b'}
# >>> d = {}.fromkeys(['Name','Phone','Email','Address'],'unknown')
# >>> d
# {'Name': 'unknown', 'Phone': 'unknown', 'Email': 'unknown', 'Address': 'unknown'}
# >>>
# >>>
# >>>
# >>> e = {}.fromkeys('abcd','value')
# >>> e
# {'a': 'value', 'b': 'value', 'c': 'value', 'd': 'value'}
# >>> e = {}.fromkeys(['abcd'],'value')
# >>> e
# {'abcd': 'value'}
# >>> e = {}.fromkeys('a',['value','val2','val3'])
# >>> e
# {'a': ['value', 'val2', 'val3']}
# >>> e['a]
#   File "<stdin>", line 1
#     e['a]
#         ^
# SyntaxError: EOL while scanning string literal
# >>> e['a']
# ['value', 'val2', 'val3']
# >>>
# >>>
# >>>
# >>>
# >>> d = dict(a=22, b=33, c=44, d=55)
# >>>
# >>>
# >>>
# >>> d
# {'a': 22, 'b': 33, 'c': 44, 'd': 55}
# >>> d['a']
# 22
# >>> d['b']
# 33
# >>> d['x']
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# KeyError: 'x'
# >>>
# >>> d.get('a')
# 22
# >>> d.get('b')
# 33
# >>> d.get('x')
# >>> print(d.get('x'))
# None
# >>> z = d.get('x')
# >>> z
# >>> z is None
# True
# >>>
# >>>
# >>>
# >>>
# >>> d
# {'a': 22, 'b': 33, 'c': 44, 'd': 55}
# >>> l = [1,2,3,44]
# >>> l
# [1, 2, 3, 44]
# >>> l.pop()
# 44
# >>>
# >>>
# >>>
# >>> d
# {'a': 22, 'b': 33, 'c': 44, 'd': 55}
# >>> d.pop()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: pop expected at least 1 arguments, got 0
# >>> d.pop('a')
# 22
# >>> d
# {'b': 33, 'c': 44, 'd': 55}
# >>> d.pop('d')
# 55
# >>> d.pop('x')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# KeyError: 'x'
# >>>
# >>>
# >>>
# >>> d.pop()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: pop expected at least 1 arguments, got 0
# >>>
# >>>
# >>>
# >>> d = dict(a=22, b=33, c=44, d=55)
# >>>
# >>>
# >>>
# >>> d
# {'a': 22, 'b': 33, 'c': 44, 'd': 55}
# >>> d.popitem()
# ('d', 55)
# >>> d.popitem('a')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: popitem() takes no arguments (1 given)
# >>>
# >>>
# >>>
# >>>
# >>>
# >>> d
# {'a': 22, 'b': 33, 'c': 44}
# >>> d.popitem()
# ('c', 44)
# >>> d
# {'a': 22, 'b': 33}
# >>>
# >>>
# >>>
# >>> d = dict(a=22, b=33, c=44, d=55)
# >>> d
# {'a': 22, 'b': 33, 'c': 44, 'd': 55}
# >>> e = {}
# >>> type(e)
# <class 'dict'>
# >>>
# >>>
# >>>
# >>> d
# {'a': 22, 'b': 33, 'c': 44, 'd': 55}
# >>> e
# {}
# >>> e.update(d)
# >>> e
# {'a': 22, 'b': 33, 'c': 44, 'd': 55}
# >>>
# >>>
# >>>
# >>> e['d']=66
# >>> e
# {'a': 22, 'b': 33, 'c': 44, 'd': 66}
# >>> d
# {'a': 22, 'b': 33, 'c': 44, 'd': 55}
# >>>
# >>>
# >>>
# >>> e = {}
# >>> e['key':'value']
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: unhashable type: 'slice'
# >>> e['key']='value'
# >>> e
# {'key': 'value'}
# >>>
# >>>
# >>>
# >>>
# >>> e
# {'key': 'value'}
# >>> d
# {'a': 22, 'b': 33, 'c': 44, 'd': 55}
# >>> e.update(d)
# >>> e
# {'key': 'value', 'a': 22, 'b': 33, 'c': 44, 'd': 55}
# >>> e = d.copy()
# >>> e
# {'a': 22, 'b': 33, 'c': 44, 'd': 55}
# >>>
# >>>
# >>>
# >>>
# >>>
# >>>
# >>>
# >>> d
# {'a': 22, 'b': 33, 'c': 44, 'd': 55}
# >>> e
# {'a': 22, 'b': 33, 'c': 44, 'd': 55}
# >>> e['a'] = 2222
# >>> e['d'] = 5555
# >>>
# >>> e
# {'a': 2222, 'b': 33, 'c': 44, 'd': 5555}
# >>> d
# {'a': 22, 'b': 33, 'c': 44, 'd': 55}
# >>>
# >>> e['x'] = 12321
# >>> e
# {'a': 2222, 'b': 33, 'c': 44, 'd': 5555, 'x': 12321}
# >>> d
# {'a': 22, 'b': 33, 'c': 44, 'd': 55}
# >>>
# >>>
# >>>
# >>> e.update(d)
# >>> e
# {'a': 22, 'b': 33, 'c': 44, 'd': 55, 'x': 12321}
# >>>
# >>>
# >>>
# >>> x = [i for i in range(10)]
# >>> x
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# >>>
# >>>
# >>>
# >>>
