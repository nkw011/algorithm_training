# https://nkw011.github.io/baekjoon/baekjoon-5582/

import sys
def input(): return sys.stdin.readline().rstrip()

s1, s2 = input(), input()
subs = [[0] * len(s2) for _ in range(len(s1))]

for i in range(len(s1)):
    for j in range(len(s2)):
        if s1[i] == s2[j]:
            subs[i][j] = 1 
            if i-1 >= 0 and j-1 >= 0:
                subs[i][j] += subs[i-1][j-1]
            
print(max([max(arr) for arr in subs]))
