import numpy as np
import numpy.linalg as lin

def to_array(s):
    out = []
    for l in s.split('\n'):
        o = []
        for n in l.split(' '):
            o.append(int(n))
        out.append(o)
    return out

ms = """8 16 -8
16 17 2
-8 2 -4"""

def t(m):
    return np.transpose(m)

def inv(m):
    return lin.inv(m)

def id(n):
    return np.identity(n)

def mul(m,n):
    return np.matmul(m,n)

m = np.array(to_array(ms))

diag = np.identity(3)

v = inv(mul(mul(t(id(3)),inv(m)),id(3)))

print(v)