import math

def f_1(x):
    """f(x) = x^3 + 1"""
    return (x**3+1)

def Df_1(x):
    """d/dx(x^3 + 1) = 3 x^2"""
    return (3*x**2)

def f_2(x):
    """x^5 sin(x)"""
    return(x**5*math.sin(x))

def Df_2(x):
    """d/dx(x^5 sin(x)) = x^4 (5 sin(x) + x cos(x))"""
    return(x**4 *( 5*math.sin(x) + x*math.cos(x) ))
