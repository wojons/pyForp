pyForp
======

Python implentation of forp written for PHP
The orginal PHP project can be found here https://github.com/aterrien/forp
The output of this one should match the orginal project, I wrote it in a few hours and have not had enough time to test it the UI yet

How-To
======
Python :
```python
import pyForp

def fib(n):
    if n < 2:
        return n
    return fib(n-2) + fib(n-1)

forp = pyForp.pyForp()
forp.start()
print fib(2)
forp.stop()
print forp.dump()
```
Result :
```
{   'idrss': 0,
    'inblock': 0,
    'isrss': 0,
    'ixrss': 0,
    'majflt': 0,
    'maxrss': 52,
    'minflt': 11,
    'msgrcv': 0,
    'msgsnd': 0,
    'nivcsw': 2,
    'nsignals': 0,
    'nswap': 0,
    'nvcsw': 0,
    'oublock': 0,
    'stack': {   0: {   'bytes': 72,
                        'file': '',
                        'function': '{main}',
                        'level': 0,
                        'pusec': 0,
                        'usec': 0},
                 1: {   'args': {   'n': 2},
                        'bytes': 6332416,
                        'class': None,
                        'file': 'test.py',
                        'function': 'fib',
                        'level': 3,
                        'lineno': 4,
                        'parent': 1,
                        'pusec': 10.017014265060425,
                        'usec': 676.8703460693359},
                 2: {   'args': {   'n': 0},
                        'bytes': 6332416,
                        'class': None,
                        'file': 'test.py',
                        'function': 'fib',
                        'level': 4,
                        'lineno': 4,
                        'parent': 2,
                        'pusec': 14.066970348358154,
                        'usec': 15.974044799804688},
                 3: {   'args': {   'n': 1},
                        'bytes': 6332416,
                        'class': None,
                        'file': 'test.py',
                        'function': 'fib',
                        'level': 4,
                        'lineno': 4,
                        'parent': 3,
                        'pusec': 10.967570543289185,
                        'usec': 15.974044799804688}},
    'stime': 0.0,
    'utime': 0.0040000000000000036}
```
