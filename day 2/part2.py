f=open('day2.txt', 'r')
lool=['A','B','C']
wynik=0
for line in f:
    y=line[2]
    x=line[0]
    if y=='X':
        wynik=wynik+0
        y=lool[(int(lool.index(x))-1)%3]
    elif y=='Y':
        wynik=wynik+3
        y=x
    elif y=='Z':
        wynik = wynik +6
        y=lool[(lool.index(x)+1)%3]
    if y=='A':
        wynik=wynik+1
    elif y=='B':
        wynik=wynik+2
    elif y=='C':
        wynik = wynik +3

print(wynik)