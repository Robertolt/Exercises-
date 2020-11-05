"""To be a triangle, it's necessary to prove that:
|b-c| < a < b+c
|a-c| < b < a+c
|b-a| < c < b+a
a,b and c are the sides.
if a=b=c must be a equilateral triangle
if a=!b=!c must be a scalene triangle
if a=b=!c must be a isoceles triangle
"""
l1 = float(input('Type on the length of side 1: '))
l2 = float(input('Type on the length of side 2: '))
l3 = float(input('Type on the length of side 3: '))

import math
from math get fabs

if fabs(l2 - l3) < l1 < (l2+ l3) and (l1 - l3) < l2 < (l1 + l3) and (l2 - l1) < l3 < (l2 + l1):
    elif {l1 = l2, l1 = l3, l2 = l3}
    print('equilateral')
