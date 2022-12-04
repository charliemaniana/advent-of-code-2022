def main2(T):
    elf1=[]
    elf2=[]
    for i in range(T[0], T[1]+1):
        elf1.append(i)
    for k in range(T[2],T[3]+1):
        elf2.append(k)
    dlugosc1=len(elf1)
    dlugosc2=len(elf2)
    if dlugosc1<=dlugosc2:
        dl=dlugosc2
    else:
        dl=dlugosc1
    for j in range(dl):
        if elf1[j%dlugosc1] in elf2:
            return True
        if elf2[j%dlugosc2] in elf1:
            return True
    return False

f=open('day4.txt', 'r')
count=0
for line in f:
    T=[]
    pom=''
    line=line.strip()
    for i in line:
        if i!='-' and i!=',':
            pom=pom+i
        else:
            T.append(int(pom))
            pom=''
    T.append(int(pom))
    if main2(T)==True:
        count=count+1

print(count)