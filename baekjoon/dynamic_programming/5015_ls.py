# asterisk가 과연 몇개의 문자와 매칭이 되는지가 관건

import sys
def input(): return sys.stdin.readline().rstrip()


def matching(i, j):
    l, r = i, j
    if dp[i][j] != -1:
        return dp[i][j]
    dp[i][j] = 1
    while l < leng1 and r < leng2:
        if wild[r] == '*':
            break
        if string[l] != wild[r]:
            dp[i][j] = 0
            return dp[i][j]
        l += 1
        r += 1
    if r < leng2 and wild[r] == '*':
        for k in range(l, leng1+1):
            if matching(k, r+1):
                return dp[i][j]
        dp[i][j] = 0
    if l >= leng1 and r < leng2:
        dp[i][j] = 0
    if l < leng1 and r >= leng2 and wild[r-1] != '*':
        dp[i][j] = 0
    return dp[i][j]


wild = input()
leng2 = len(wild)
n = int(input())
for _ in range(n):
    string = input()
    leng1 = len(string)
    dp = [[-1] * (leng2+1) for _ in range(leng1+1)]
    if matching(0, 0):
        print(string)
