import sys
input = sys.stdin.readline

n,k =  map(int,input().split())
dp1 = [0] * (n-2)
dp2 = [0] * (n-2)
dp1[:2] = [1,1]
dp2[:2] = [1,2]

for i in range(2,n-2):
    dp1[i] = dp1[i-1] + dp1[i-2]
    dp2[i] = dp2[i-1] + dp2[i-2]
    
a = 1
b = 0
while True:
    result = dp1[n-3] * a
    if (k - result) % dp2[n-3] == 0:
        b = (k - result) // dp2[n-3]
        break
    a +=1
print(a)
print(b)