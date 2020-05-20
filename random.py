cow=0
bull=0
counter=1
b=1256
c=str(b)
while cow!=4:
    a=input('enter the number')
    d=str(a)
    for i in range(0,len(d)):
        for k in range(0,len(c)):
            if i==k and d[i]==c[k]:
                cow+=1
            elif i!=k and d[i]==c[k]:
                bull+=1
            else:
                pass
    print('cows:',cow,'bulls:',bull)
    if cow==4:
        break
    cow=0
    bull=0
    counter+=1

print('you won in:',counter,'tries')
        
    
