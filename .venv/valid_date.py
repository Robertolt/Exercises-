month = int(input('input the number of the month: '))
day = int(input('input the day as a number: '))
year = int(input('input year: '))

if month >= 12:
    print('invalid date')
elif day >= 31:
    print('invalid date')
else:
    print('your date is ok fella :)')