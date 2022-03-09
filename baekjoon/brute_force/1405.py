import sys
def input(): return sys.stdin.readline().rstrip()

def dfs(e_cnt, w_cnt, n_cnt, s_cnt, y, x, N):
    global visited, result
    if N == 0:
        result += (e ** e_cnt) * (w**w_cnt) * \
            (s**s_cnt) * (n**n_cnt)
        return
    if (y-1, x) not in visited:
        visited.add((y-1, x))
        dfs(e_cnt, w_cnt, n_cnt+1, s_cnt, y-1, x, N-1)
        visited.remove((y-1, x))
    if (y+1, x) not in visited:
        visited.add((y+1, x))
        dfs(e_cnt, w_cnt, n_cnt, s_cnt+1, y+1, x, N-1)
        visited.remove((y+1, x))
    if (y, x+1) not in visited:
        visited.add((y, x+1))
        dfs(e_cnt+1, w_cnt, n_cnt, s_cnt, y, x+1, N-1)
        visited.remove((y, x+1))
    if (y, x-1) not in visited:
        visited.add((y, x-1))
        dfs(e_cnt, w_cnt+1, n_cnt, s_cnt, y, x-1, N-1)
        visited.remove((y, x-1))

N, e, w, s, n = map(int, input().split())
result = 0
visited = set()
visited.add((0, 0))
dfs(0, 0, 0, 0, 0, 0, N)

print(result * 10**(-2*N))
