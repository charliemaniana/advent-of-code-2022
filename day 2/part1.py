f=open('day2.txt', 'r')
wynik=0
for line in f:
    y=line[2]
    x=line[0]
    print(x,y)
    if y=='X':
        wynik=wynik+1
    elif y=='Y':
        wynik=wynik+2
    elif y=='Z':
        wynik = wynik +3
    if x=='A' and y=='Y':
        wynik=wynik+6
    elif x=='B' and y=='Z':
        wynik=wynik+6
    elif x=='C' and y=='X':
        wynik=wynik+6
    elif x=='A' and y=='X':
        wynik=wynik+3
    elif x == 'B' and y == 'Y':
        wynik = wynik + 3
    elif x == 'C' and y == 'Z':
        wynik = wynik + 3
    else:
        pass

print(wynik)