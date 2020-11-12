number = int(input('input a number < 1000: '))


unit = (number%10)
dozens = (number%100 - unit)//10
hundreds = (number - (dozens*10+unit))//100


print('The typed number has:',hundreds,'hundreds',dozens,'dozens','and',unit,'units')

