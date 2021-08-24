import sys
input = lambda : sys.stdin.readline().rstrip()

def comb(n,m):
    if n == m or m == 0: return 1
    if dp[n][m] != -1 : return dp[n][m]
    dp[n][m] = 0
    dp[n][m] = comb(n-1,m) + comb(n-1,m-1)
    return dp[n][m]

def dictionary(n,m,k):
    if n == 0:
        for _ in range(m):
            print('z',end='')
        return
    if m == 0:
        for _ in range(n):
            print('a',end='')
        return

    if comb(n+m-1,m) >= k:
        print('a',end='')
        dictionary(n-1,m,k)
    else :
        print('z',end='')
        dictionary(n,m-1,k-comb(n+m-1,m))
        

n,m,k = map(int,input().split())
large = m if n < m else n
dp = [[-1] * (m+1) for _ in range(n+m+1)]
comb(n+m,m)
if k > comb(n+m,m): print(-1)
else :
    dictionary(n,m,k)
    print()