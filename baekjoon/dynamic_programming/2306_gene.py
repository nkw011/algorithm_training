# 겁먹지 않고 차근차근히 분석하다보면 풀 수 있는 문제
# dp같은 문제는 처음에 재귀적인 요소를 어떤걸 적용할 수 있는 지 살펴보고
# brute-force를 이용해 구현한 다음에 dp를 이용해 시간을 단축한다.
# 재귀함수를 풀 때 중요한 것은 한 번에 하나만을 이용해서 구한다는 점이다.

import sys
def input(): return sys.stdin.readline().rstrip()


def koiDNA(i, j):
    if i == j:
        return 0
    if dp[i][j] != -1:
        return dp[i][j]
    dp[i][j] = 0
    if (s[i] == 'a' and s[j] == 't') or (s[i] == 'g' and s[j] == 'c'):
        dp[i][j] = max(dp[i][j], 2 + koiDNA(i+1, j-1))
    for k in range(i, j):
        dp[i][j] = max(dp[i][j], koiDNA(i, k)+koiDNA(k+1, j))
    return dp[i][j]


s = input()
leng = len(s)
dp = [[-1] * leng for _ in range(leng)]
print(koiDNA(0, leng-1))
