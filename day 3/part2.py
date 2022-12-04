def main2(a,b,c):
    odp=0
    for z in range(len(a)):
        if a[z] in b and a[z] in c:
            odp=alfabet.index(a[z])
    return odp



priority=0
f=open('day3.txt', 'r')
alfabet=' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
suma=0
licznik = 0
a=''
b=''
c=''
for line in f:
    line=line.strip()
    if licznik!=3:
        if a=='':
            a=line
        elif b=='':
            b=line
        elif c=='':
            c=line
        licznik=licznik+1
        if licznik == 3:
            suma = suma + main2(a, b, c)
            licznik = 0
            a = ''
            b = ''
            c = ''

print(suma)


