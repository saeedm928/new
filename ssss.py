a='aaaa bbbb cccc dddd'
l=a.split()
o=[]
for i in range(len(l)-1,-1,-1):
    o.append(l[i])
w=''
for i in o:
    w+=i+' '
print(w)
    
    
