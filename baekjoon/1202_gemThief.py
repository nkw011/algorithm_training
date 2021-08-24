# 이런 식으로 사용할 수 있는 지는 전혀몰랐다.
# 어쨌든 무게를 가지고 있기 때문에 물건과 가방을 같이 몰아넣고
# 무게순으로 오름차순 정렬을 한다. 그 이후에 가방이 하나씩 나올 때까지 물건들을 pq에 넣고
# 가방이 나오면 값이 가장 비싼 물건을 하나씩 뽑아서 넣는다.
# 단 물건이 없으면 그대로 뽑지 않는다. (이 의미는 가방 갯수가 많다면 가방에 들어갈 물건이 없다는 뜻이다.)

import sys
import heapq
INF = int(1e7)
def input(): return sys.stdin.readline().rstrip()


n, k = map(int, input().split())
q = []
allThing = []

for _ in range(n):
    a, b = map(int, input().split())
    allThing.append((a, b))

for _ in range(k):
    a = int(input())
    allThing.append((a, INF))
allThing.sort(key=lambda x: x[0])

result = 0
size = 0
for w, p in allThing:
    if p != INF:
        heapq.heappush(q, -p)
        size += 1
    else:
        if size > 0:
            result += heapq.heappop(q)
            size -= 1

print(-result)
