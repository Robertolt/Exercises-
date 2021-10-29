"""Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais.
Valide a entrada e permita repetir a operação."""

print('''insert 2 populations sizes and their growthing rates so the program will calculate the time in years one will '
reach the other''')

while True:

    year = 0

    while True:
        try:
            popA = float(input('input the population A: '))
            popB = float(input('input the population B: '))
            growth_rate_a = float(input('input the population A growth rate in %: '))/100
            growth_rate_b = float(input('input the population B growth rate in %: '))/100
        except ValueError:
            print('please insert a float or integer number')
        else:
            if popA > popB and growth_rate_a >= growth_rate_b:
                print('Population B will never reach population A')
                break
            elif popB > popA and growth_rate_b >= growth_rate_a:
                print('Population A will never reach population B')
                break
            elif popA > popB and growth_rate_b > growth_rate_a:
                while popA >= popB:
                    popA = popA*(1 + growth_rate_a)
                    popB = popB*(1 + growth_rate_b)
                    year += 1
                break
            elif popB > popA and growth_rate_a > growth_rate_b:
                while popB >= popA:
                    popA = popA*(1 + growth_rate_a)
                    popB = popB*(1 + growth_rate_b)
                    year += 1
                break

    if year == 0:
        pass
    elif year == 1:
        print(f'will take {year} year')
    else:
        print(f'will take {year} years')

    finish_line = str(input('Do you want to restart the program?(y/n): '))
    if finish_line == 'y':
        pass
    else:
        break
