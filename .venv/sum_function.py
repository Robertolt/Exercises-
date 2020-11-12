def sum_numbers(*s):

    """
     >>> sum_numbers(1,2,3)
    6

    >>>sum(54,67,108)
    229

    :param s:
    :return:
    """

    aux = 0
    for valor in s:
        aux += valor
    return(aux)

if __name__ == '__main__':
    sum_numbers(int(input()))
    print(aux)