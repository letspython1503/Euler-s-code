def is_palindrome(n):
    n=str(n)
    if len(n)%2!=0:
        return False
    else:
        n=str(n)
        x1=len(n)//2
        if n[0:x1] == n[:x1-1:-1]:
            return True
def get_answer(n):
    upperlimit = (10**n)-1
    lowerlimit = (10**(n-1))
    for i in range(upperlimit,lowerlimit,-1):
        for j in range(upperlimit,lowerlimit,-1):
            if i>j:
                if is_palindrome(i*j):
                    return i*j
print(get_answer(7))
