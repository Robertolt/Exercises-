"""To be a triangle, it's necessary to prove that:
|b-c| < a < b+c
|a-c| < b < a+c
|b-a| < c < b+a
a,b and c are the sides.
if a=b=c must be a equilateral triangle
if a=!b=!c must be a scalene triangle
if a=b=!c must be a isoceles triangle"""

print('input the sides of your triangle:')
la = int(input('la:'))
lb = int(input('lb:'))
lc = int(input('lc:'))

if la == lb and la == lc:
    print('equilateral triangle')
elif (la == lb) or ( lb == lc) or (la==lc):
    print('isoceles triangle')
else:
    print('scalene triangle')

