import sys
def input(): return sys.stdin.readline().rstrip()

n,m = map(int, input().split())
words = [input().rstrip() for _ in range(n)]

cols = []
for j in range(m):
    col = ''
    for i in range(n):
        col += words[i][j]
    cols.append(col)

cnt = 0
for i in range(1,n):
    sub_cols = set()
    for j in range(m):
        sub_cols.add(cols[j][i:])
    if len(sub_cols) != m:
        break
    cnt += 1
print(cnt)
