import random
a=int(input())
while(a==1):
    n=random.randint(0,100)
    if(n<100):
        print(n,end='')

    else:
        print(n)
        break
