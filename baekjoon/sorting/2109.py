# 해설: https://nkw011.github.io/baekjoon/baekjoon-219/

import sys
import heapq
def input(): return sys.stdin.readline().rstrip()

# 단순하게 접근하자. 해당 일자에서 얻을 수 있는 최댓값을 고른다.

n = int(input())
q = []
lecture = [tuple(map(int,input().split())) for _ in range(n)]
lecture.sort(key=lambda x: -x[1])
days = [-1] * 10001
for i, lec in enumerate(lecture):
    _, d = lec
    days[d] = i
q,last,result = [],0,0
for d in range(10000,0,-1):
    if days[d] != -1:
        for j in range(last, days[d] +1):
            heapq.heappush(q,-lecture[j][0])
        last = days[d] + 1
    if q:
        result += -heapq.heappop(q)
print(result)


################# 두번째 풀이 #################

n = int(input())
lecture = [tuple(map(int,input().split())) for _ in range(n)]
lecture.sort(key=lambda x: (-x[0],-x[1]))
day = [0] * 10001

for p, d in lecture:
    for j in range(d,0,-1):
        if day[j] == 0:
            day[j] = p
            break

print(sum(day))
