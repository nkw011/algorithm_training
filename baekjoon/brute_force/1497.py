import sys
from itertools import combinations
def input(): return sys.stdin.readline().rstrip()


n, m = map(int, input().split())
visited = [0] * m
guitar = [[0] * m for _ in range(n)]

for i in range(n):
    _, song = input().split()
    for j in range(m):
        if song[j] == 'Y':
            guitar[i][j] = 1

max_song, count = 0, 0
for cnt in range(1, n+1):
    for array in combinations(list(range(n)), cnt):
        visited = [0] * m
        for g in array:
            for i in range(m):
                visited[i] = max(visited[i], guitar[g][i])
        num_song = sum(visited)
        if num_song > max_song:
            max_song = num_song
            count = cnt
        elif num_song == max_song and cnt < count:
            count = cnt
if count == 0:
    print(-1)
else:
    print(count)
