# https://m.blog.naver.com/PostView.nhn?blogId=kks227&logNo=221386454504&proxyReferer=https:%2F%2Fwww.google.com%2F
# 이 문제는 도저히 못 풀겠어서 출처에 적힌 풀이를 참고하여 풀었다.

import sys
def input(): return sys.stdin.readline().rstrip()


n, m = map(int, input().split())
jew = [int(input()) for _ in range(n)]
pSum = [0] * (n+1)

for i in range(n):
    pSum[i+1] = pSum[i] + jew[i]

result, temp = 0, 0
for i in range(m-1, n):
    temp = min(temp, pSum[i-m+1])
    result = max(result, pSum[i+1]-temp)

print(result)
