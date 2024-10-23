def fib_prob2(z):
    n=0
    sum1=2
    l=[1,2]
    while True:
        a=l[-2]+l[-1]
        if a>z:
            break
        if a%2==0:
            sum1+=a
        l.append(a)
        n+=1
    return sum1
z=int(input('Enter the required number:'))
print(fib_prob2(z))