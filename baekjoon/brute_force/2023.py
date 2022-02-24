import sys
def input(): return sys.stdin.readline().rstrip()

def is_prime(num):
    if num <= 1: return False
    if num == 2: return True
    for k in range(3,(int(num**(1/2))+1)):
        if num % k == 0:
            return False
    return True

n = int(input())

n_prime = { i:[] for i in range(1,n+1)}
n_prime[1] = [2,3,5,7]

for i in range(2,n+1):
    for num in n_prime[i-1]:
        for j in range(1,10,2):
            if is_prime(num * 10 + j):
                n_prime[i].append(num*10+j)
                
for i in n_prime[n]:
    print(i)
