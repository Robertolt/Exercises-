"""To be a triangle, it's necessary to prove that:
|b-c| < a < b+c
|a-c| < b < a+c
|b-a| < c < b+a
a,b and c are the sides.
if a=b=c must be a equilateral triangle
if a=!b=!c must be a scalene triangle
if a=b=!c must be a isoceles triangle"""

print('input the sides of your triangle:')
la = print(input('la:'))
lb = print(input('lb:'))
lc = print(input('lc:'))

if la == lb == lc:
        print('equilateral triangle')
elif la != lb != lc:
        print('scalene triangle')
else:
        print('isoceles triangle')

