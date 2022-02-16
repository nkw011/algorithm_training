# Var(X) = E[X^2] - (E[X])^2
# p_sum = [0] * (n+1)
# p_square = [0] * (n+1)
# for i in range(1, n+1):
#     p_sum[i] = p_sum[i-1] + doll[i]
#     p_square[i] = p_square[i-1] + (doll[i]**2)

import sys
import math
def input(): return sys.stdin.readline().rstrip()


def variance(arr):
    avg = sum(arr) / len(arr)
    var = 0
    for n in arr:
        var += (n-avg)**2
    return var / len(arr)


n, k = map(int, input().split())
doll = list(map(int, input().split()))

answer = []
for window in range(k, n+1):
    for i in range(n-window+1):
        answer.append(variance(doll[i:i+window]))
print(math.sqrt(min(answer)))
