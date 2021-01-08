n1 = float(input('type on the 1 number: '))
n2 = float(input('type on the 2 number: '))
n3 = float(input('type on the 3 number: '))

if n1 > n2 and n1 > n3:
    print(n1)
elif n2 > n1 and n2 > n3:
    print(n2)
else:
    print(n3)


