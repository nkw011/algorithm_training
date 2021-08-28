import sys
INF = int(1e4)
def input(): return sys.stdin.readline().rstrip()


sys.setrecursionlimit(100000)


def cntPalindrome(i):
    global leng
    if i >= leng:
        return 0
    if dp[i][leng-1]:
        return 1
    if dp2[i] != -1:
        return dp2[i]
    dp2[i] = INF
    for k in range(i, leng):
        if dp[i][k]:
            dp2[i] = min(dp2[i], 1+cntPalindrome(k+1))
    return dp2[i]


s = input()
leng = len(s)

dp = [[-1] * leng for _ in range(leng)]
dp2 = [-1] * leng

# dp[i][j] : s[i:j+1]이 펠린드롬인지 확인함
for j in range(leng):
    for i in range(j+1):
        if i == j:
            dp[i][j] = 1
        elif s[i] == s[j]:
            if i+1 <= j-1:
                dp[i][j] = dp[i+1][j-1]
            else:
                dp[i][j] = 1
        else:
            dp[i][j] = 0

print(cntPalindrome(0))
