print('\nDescrição:\n1-Valor y da sequência\n2-Valor z da sequência\n')
while True:
    x=list(map(int,input(': ').split()))
    if len(x)<1:
        break
    print('Soma de todos os números entre {} e {}:'.format(x[0],x[1]))  
    if x[0]>x[1]:
        x[0]-=x[1]
        x[1]+=x[0]
        x[0]=x[1]-x[0]
    temp=0
    if (x[1]-x[0]+1)%2!=0:
        temp=(x[0]+x[1]-1)*int((x[1]-x[0]+1)/2)+x[1]
    else:
        temp=(x[0]+x[1])*(x[1]-x[0]+1)/2
    print('{:.0f}'.format(temp))
print("Até!\n")