import math



a = float(input('Input a number for a'))
if a==0:
    print('not a second degree equation')
else:
    b = float(input('Input a number for b'))
    c = float(input('Input a number for c'))
    delta = ((b*b)-(4*a*c))


    if delta < 0:
        print('the equation doesnt have real answers')
    elif delta == 0:
        answer_0 = (-b/2*a)
        print('the equation has one real answer', answer_0)
    else:
        answer_1 = (-b + math.sqrt(delta)) / (2 * a)
        answer_2 = (-b - math.sqrt(delta)) / (2 * a)
        print('the equation has 2 real answers', answer_1, answer_2)
