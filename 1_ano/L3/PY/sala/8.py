print()
while True:
    if len(x:=input('Insira n indíce de fibonacci: '))<1:
        break
    a,b,c=0,1,0
    for i in range(1,int(x)):
        a=b+c
        c=b
        b=a
    print(b)
print('Até!\n')