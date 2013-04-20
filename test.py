import pyForp
import pprint
pp = pprint.PrettyPrinter(indent=4)
def fib(n):
    if n < 2:
        return n
    return fib(n-2) + fib(n-1)

forp = pyForp.pyForp()
forp.start()
print fib(2)
forp.stop()
pp.pprint(forp.dump())
