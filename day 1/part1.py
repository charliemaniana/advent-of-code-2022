f=open('day1.txt', 'r')
snacks=[]
energy=0
for krasnal in f:
    if krasnal=='\n':
        snacks.append(energy)
        energy=0
    else:
        energy=energy+int(krasnal)
print(max(snacks)()
