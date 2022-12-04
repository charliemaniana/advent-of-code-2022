def main1(T):
    if T[0]>=T[2] and T[1]<=T[3]:
        return True
    if T[0]<=T[2] and T[1]>=T[3]:
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
    if main1(T)==True:
        count=count+1

print(count)