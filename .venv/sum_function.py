"""Give numbers and make the progam sum it and return for you"""

print('Type on the wished numbers like these: 1,2,174 ')



def soma(*args):
    aux = 0
    for vallue in args:
        aux =+ vallue
    return aux


if __name__ == '__main__':


