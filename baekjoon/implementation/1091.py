# 풀이 및 해설: https://nkw011.github.io/baekjoon/baekjoon-1091/

# 두번째 풀이
# 144272KB	308ms
import sys
def input(): return sys.stdin.readline().rstrip()

n = int(input())
P = input().split()
S = list(map(int,input().split()))

visited = set()
answer,cnt = '012' * (n//3), 0
while True:
    seq = "".join(P)
    if seq == answer:
        break
    if seq in visited:
        cnt = -1
        break
    visited.add(seq)
    temp = [0] * n
    for i in range(n):
        temp[S[i]] = P[i]
    P = temp
    cnt += 1
print(cnt)

# 첫번째 풀이
# 275216KB	672ms
import sys
from collections import defaultdict
def input(): return sys.stdin.readline().rstrip()

n = int(input())
P = list(map(int,input().split()))
S = list(map(int,input().split()))

answer = defaultdict(set)
visited = set()

for i in range(n):
    answer[P[i]].add(i)

cnt = 0
cards = list(range(n))
while True:
    first,second,third = set(cards[0:n:3]), set(cards[1:n:3]), set(cards[2:n:3])
    if first == answer[0] and second == answer[1] and third == answer[2]:
        break
    if tuple(cards) in visited:
        cnt = -1
        break
    visited.add(tuple(cards))
    temp = [0] * n
    for i in range(n):
        temp[S[i]] = cards[i]
    cards = temp
    cnt += 1
print(cnt)
