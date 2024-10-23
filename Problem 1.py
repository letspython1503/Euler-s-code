import math
def final_answer(n):
    l=[]
    for i in range(1,n):
        if i*3 >= n and i*5 >= n:
            break
        elif i*3 <= n and i*5 >= n:
            l.append(i*3)
        else:
            l.append(i*3)
            l.append(i*5)       
    return sum(list(set(l)))
n=int(input('Enter the required number'))
print(final_answer(n))
