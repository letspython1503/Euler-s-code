import math
def get_maxprimefactor(n):
    final=2
    while n%2==0:
        n/=2
    for i in range(3,int(math.sqrt(n))+1,2):
        while n%i==0:
            final=i
            n/=i
    if n>2:
        if n>final:
            final=n
    return int(final)
n1=int(input('Enter the required number'))
print(get_maxprimefactor(n1))