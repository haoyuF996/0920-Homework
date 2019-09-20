def pyramid(): 
    char,num = input('An character:'),int(input('An odd number:'))
    for i in range(1,num+2,2):
        print(' '*((num-i)//2)+char*i)
def stupid_pyramid():
    symbol = input('Symbol:')#string
    Maxnumber = int(input('Maxnumber:'))#integer
    while (-1)**Maxnumber != -1:
        print('An odd number is expected.')
        Maxnumber = int(input('Maxnumber:'))
    NumberOfSpace = (Maxnumber-1)//2#integer
    NumberOfSymbol = 1#integer
    while NumberOfSymbol<=Maxnumber:
        for i in range(NumberOfSpace):
            print(' ',end='')
        for i in range(NumberOfSymbol):
            print(symbol,end='')
        print()
        NumberOfSpace-=1
        NumberOfSymbol+=2
def hollow_pyramid():
    char,num = input('An character:'),int(input('An odd number:'))
    print(' '*int((num-1)/2)+char)
    for i in range(3,num,2):
        print(' '*((num-i)//2)+char+' '*(i-2)+char)
    print(char*num)
if __name__ == "__main__":
    choice = input('Stupid,Normal or Hollow:(S/N/H)')
    if choice == 'S':
        stupid_pyramid()
    elif choice == 'N':
        pyramid()
    else:
        hollow_pyramid()