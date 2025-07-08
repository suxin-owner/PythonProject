#求解一元二次方程

import math

def quadratic(a, b, c):
    
    discriminant = b**2 - 4*a*c
    
    if discriminant < 0 :
        return "该方程没有实数解"
    elif discriminant == 0 :
        x = -b / (2*a)
        return x
    else :
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        return x1,x2

print(quadratic(2,3,1))