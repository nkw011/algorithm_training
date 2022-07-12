# 풀이 및 해설: https://velog.io/@nkw011/baekjoon-2042

import sys
from collections import defaultdict
def input(): return sys.stdin.readline().rstrip()

n, m, k = map(int,input().split())
nums = [0] + [int(input()) for _ in range(n)]
partial_sum = [0] * (n+1)
for i in range(1,n+1):
    partial_sum[i] = partial_sum[i-1] + nums[i]
diff = defaultdict(int)

for _ in range(m+k):
    a, b, c = map(int,input().split())
    if a == 1:
        diff[b] = c-nums[b]
    else:
        diff_b, diff_c = 0,0
        for k in diff.keys():
            if k <= b-1: diff_b += diff[k]
            if k <= c: diff_c += diff[k]
        print(partial_sum[c] + diff_c - partial_sum[b-1] - diff_b)
