"""Altere o programa anterior para mostrar no final a soma dos números."""

n1 = int(input('input the 1st integer number: '))  #ex:1
n2 = int(input('input the 2nd integer number: '))  #ex:10
sum = 0

print(list(range(n1+1, n2)))

for i in range(n1+1, n2):
    sum += i

print(sum)

