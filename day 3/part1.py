def main1(a,b):
    odp=0
    for z in range(len(a)):
        if a[z] in b:
            odp=alfabet.index(a[z])
    return odp



priority=0
f=open('day3.txt', 'r')
alfabet=' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
suma=0
for line in f:
    line=line.strip()
    a=''
    b=''
    for i in range(len(line)//2):
        a=a+line[i]
        b=b+line[i+len(line)//2]
    suma=suma+main1(a,b)

print(suma)