def h(s,k):
    if s=='s' and k=='r':
        print('roya wins')
    elif s=='s' and k=='p':
        print('saeed wins')
    elif s=='p' and k=='s':
        print('roya wins')
    elif s=='p' and k=='r':
        print('saeed wins')
    elif s=='r' and k=='p':
        print('roya wins')
    elif s=='r' and k=='s':
        print('saeed wins')
    else:
        print('tied')



i=0

while i!=1:
    f=input('what do you choose saeed?')
    s=input('what do you choose roya?')
    h(f,s)
    print('if you want to continue enter 1 othe wise enter 0')
    u=int(input())
    if u==1:
        i=0
    elif u==0:
        i=1
