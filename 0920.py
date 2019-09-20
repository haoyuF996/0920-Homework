def pyramid(): 
    char = input('An character:')
    num = int(input('An odd number:'))
    for i in range(1,num+2,2):
        print(' '*int((num-i)/2)+char*i)
def stupid_pyramid():
    symbol = input('Symbol:')#string
    Maxnumber = int(input('Maxnumber:'))#integer
    while (-1)**Maxnumber != -1:
        print('An odd number is expected.')
        Maxnumber = int(input('Maxnumber:'))
    NumberOfSpace = int((Maxnumber-1)/2)#integer
    NumberOfSymbol = 1#integer
    while NumberOfSymbol<=Maxnumber:
        for i in range(NumberOfSpace):
            print(' ',end='')
        for i in range(NumberOfSymbol):
            print(symbol,end='')
        print()
        NumberOfSpace-=1
        NumberOfSymbol+=2
if __name__ == "__main__":
    if input('Stupid or not?')=='stupid':
        stupid_pyramid()
    else:
        pyramid()