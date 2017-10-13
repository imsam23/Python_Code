'''
Created on Oct 13, 2017

@author: LSX1KOR
'''
"""
MRO must prevent local precedence ordering and also provide monotonicity.
It ensures that a class always appears before its parents and in case of multiple parents,
the order is same as tuple of base classes.
"""


class X: pass
class Y: pass
class Z: pass

class A(X,Y): pass
class B(Y,Z): pass

class M(B,A,Z): pass

print(M.__mro__)
#o/p=<class '__main__.M'>, <class '__main__.B'>, <class '__main__.A'>, <class '__main__.X'>, <class '__main__.Y'>, <class '__main__.Z'>, <class 'object'>)

"""
So first here It will check for current class M then left class B then it will look into Y but Y is parent of A so it will look into A .
M->B->A

After looking into A ,it will look into X
M->B->A->X

After that it will look into Y
M->B->A->X->Y
After that it will look into Z 
M->B->A->X->Y->Z
then at the end it will look into object class
M->B->A->X->Y->Z->object

"""
