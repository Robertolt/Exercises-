n1 = float(input("type on the 1 number: "))
n2 = float(input("type on the 2 number: "))
n3 = float(input("type on the 3 number: "))

if n1<n2<n3:
    print(n3,n2,n1)
elif n2<n3<n1:
    print(n1,n3,n2)
else:
    print(n2,n1,n3)
