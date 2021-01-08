n1 = float(input('Type on your grade: '))
n2 = float(input('Type on yout grade 2: '))
media = (n1+n2)/2
if media == 10:
    print('approved as a valedictoriam')
elif media >= 7:
    print('approved')
else:
    print('flunked')