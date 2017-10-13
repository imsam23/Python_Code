'''
Created on Oct 13, 2017

@author: LSX1KOR
'''
"""
In the multiple inheritance scenario, any specified attribute is searched first in the current class.
If not found, the search continues into parent classes in depth-first,
left-right fashion without searching same class twice.
"""

class Base1(object):
    def foo(self):
        print("BASE1")

class Base2(object):
    def foo(self):
        print('BASE2')

class Derived(Base2,Base1):
    pass

d=Derived()
d.foo()
#__mro__=Method Resolution Orde
#It will tell you how the search order will be
print(Derived.__mro__)
#o/p=(<class '__main__.Derived'>, <class '__main__.Base2'>, <class '__main__.Base1'>, <class 'object'>)
#so it will look first into current class then left i.e, Base2 then Base1 then object class
