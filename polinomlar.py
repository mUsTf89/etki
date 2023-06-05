"""
def p(x):
    return x**4-4*x**2+3*x
for x in [-1,-0.5, 0, 0.0, 1]:
    print(x,p(x))
import numpy as np
import matplotlib.pyplot as plt
X=np.linspace(-3,3,50)
F=p(X)
plt.plot(X,F)
plt.show()
"""
"""
class Polynomial():
    def __init__(self,*coefficient):
        self.coefficient=list(coefficient)
    def __repr__(self):
        return "Polynomial" + str(tuple(self.coefficient))
    def __str__(self):
        def x_expr(degree):
            if degree==0:
                res=""
            elif degree==1:
                res="x"
            else:
                res="x^"+ str(degree)
            return res
        degree=len(self.coefficient)-1
        res=""
        for i in range(0,degree+1):
            coeff=self.coefficient[i]
            if abs(coeff)==1 and i<degree:
                res+=f"{'+' if coeff >0 else '-'}{x_expr(degree-i)}"
            elif coeff!=0:
                res+=f"{coeff:+}{x_expr(degree-i)}"
        return res.lstrip('+') #moving leading '+'

print(Polynomial(3,-5,50,0))
"""
"""
class Polynomial:
    def __init__(self, *coefficients):
        self.coefficients = list(coefficients)  # tuple is turned into a list
    def __call__(self, x):
        res = 0
        for index, coeff in enumerate(self.coefficients[::-1]):
            res += coeff * x ** index
        return res
#Artık sınıfımızın bir örneğini
# bir fonksiyon gibi çağırmak mümkün.
p = Polynomial(3, 0, -5, 2, 1)
print(p)
for x in range(-3, 3):
    print(x, p(x))
import matplotlib.pyplot as plt
import numpy as np
X = np.linspace(-1.5, 1.5, 50, endpoint=True)
F = p(X)
plt.plot(X, F)
plt.show()
class Polynomial2:
    def __init__(self, *coefficients):
        self.coefficients = list(coefficients)  # tuple is turned into a list
    # The __repr__ and __str__ method can be included here,
    # but is not necessary for the immediately following code
    def __call__(self, x):
        res = 0
        for coeff in self.coefficients:
            res = res * x + coeff
        return res
p1 = Polynomial(-4, 3, 0)
p2 = Polynomial2(-4, 3, 0)
res = all((p1(x)==p2(x) for x in range(-10, 10)))
print(res)
p1 = (2,)
p2 = (-1, 4, 5)
import itertools as itt
for x in itt.zip_longest(p1, p2, fillvalue=0):
    print(x)
"""
"""
import numpy as np
import matplotlib.pyplot as plt
from itertools import zip_longest
class Polynomial:
    def __init__(self, *coefficients):
        self.coefficients = list(coefficients)  # tuple is turned into a list
    def __repr__(self):
        return "Polynomial" + str(self.coefficients)
    def __call__(self, x):
        res = 0
        for coeff in self.coefficients:
            res = res * x + coeff
        return res
    def degree(self):
        return len(self.coefficients)
    def __add__(self, other):
        c1 = self.coefficients[::-1]
        c2 = other.coefficients[::-1]
        res = [sum(t) for t in zip_longest(c1, c2, fillvalue=0)]
        return Polynomial(*res[::-1])
    def __sub__(self, other):
        c1 = self.coefficients[::-1]
        c2 = other.coefficients[::-1]

        res = [t1 - t2 for t1, t2 in zip_longest(c1, c2, fillvalue=0)]
        return Polynomial(*res[::-1])
p1 = Polynomial(4, 0, -4, 3, 0)
p2 = Polynomial(-0.8, 2.3, 0.5, 1, 0.2)

p_sum = p1 + p2
p_diff = p1 - p2

X = np.linspace(-3, 3, 50, endpoint=True)
F1 = p1(X)
F2 = p2(X)
F_sum = p_sum(X)
F_diff = p_diff(X)
plt.plot(X, F1, label="F1")
plt.plot(X, F2, label="F2")
plt.plot(X, F_sum, label="F_sum")
plt.plot(X, F_diff, label="F_diff")

plt.legend()
plt.show()
"""
from itertools import zip_longest
import numpy as np
import matplotlib.pyplot as plt
class Polynomial:
    def __init__(self, *coefficients):
        self.coefficients = list(coefficients)  # tuple is turned into a list
    def __repr__(self):
        """
        method to return the canonical string representation
        of a polynomial.
        """
        return "Polynomial" + str(self.coefficients)
    def __call__(self, x):
        res = 0
        for coeff in self.coefficients:
            res = res * x + coeff
        return res
    def degree(self):
        return len(self.coefficients)
    def __add__(self, other):
        c1 = self.coefficients[::-1]
        c2 = other.coefficients[::-1]
        res = [sum(t) for t in zip_longest(c1, c2, fillvalue=0)]
        return Polynomial(*res)
    def __sub__(self, other):
        c1 = self.coefficients[::-1]
        c2 = other.coefficients[::-1]
        res = [t1 - t2 for t1, t2 in zip_longest(c1, c2, fillvalue=0)]
        return Polynomial(*res)
    def derivative(self):
        derived_coeffs = []
        exponent = len(self.coefficients) - 1
        for i in range(len(self.coefficients) - 1):
            derived_coeffs.append(self.coefficients[i] * exponent)
            exponent -= 1
        return Polynomial(*derived_coeffs)
    def __str__(self):
        def x_expr(degree):
            if degree == 0:
                res = ""
            elif degree == 1:
                res = "x"
            else:
                res = "x^" + str(degree)
            return res
        degree = len(self.coefficients) - 1
        res = ""
        for i in range(0, degree + 1):
            coeff = self.coefficients[i]
            # nothing has to be done if coeff is 0:
            if abs(coeff) == 1 and i < degree:
                # 1 in front of x shouldn't occur, e.g. x instead of 1x
                # but we need the plus or minus sign:
                res += f"{'+' if coeff > 0 else '-'}{x_expr(degree - i)}"
            elif coeff != 0:
                res += f"{coeff:+g}{x_expr(degree - i)}"
        return res.lstrip('+')  # removing leading '+'
p = Polynomial(-0.8, 2.3, 0.5, 1, 0.2)
p_der = p.derivative()
X = np.linspace(-2, 3, 50, endpoint=True)
F = p(X)
F_derivative = p_der(X)
plt.plot(X, F, label="F")
plt.plot(X, F_derivative, label="F_der")
plt.legend()
plt.show()
p = Polynomial(1, 2, -3, 4, -55)
p2 = Polynomial(1, 2, 3)
p_der = p.derivative()
print(p)
print(p_der)
print(p2)
p3 = p + p2
print(p3)