import sys
input = sys.stdin.readline

T = int(input().rstrip())
# 1안 - 시간 초과
# for _ in range(T):
#     n = int(input().rstrip())
#     ranks = []
#     for _ in range(n):
#         a, b = map(int,input().split())
#         ranks.append((a,b))
#     ranks.sort(key=lambda x : x[0])
#     visited = [0] * n
#     for i in range(n):
#         for j in range(i+1,n):
#             if not visited[j-1] and ranks[j][1] > ranks[i][1]:
#                 visited[j-1] = 1
#     count = 0
#     for val in visited:
#         if val == 0 :
#             count += 1
#     print(count)

# 2안 - 두번째가 순서가 내림차순이면 된다.(통과) -> 역시 조금 더 길게 생각해야한다.
for _ in range(T):
    n = int(input().rstrip())
    ranks = []
    for _ in range(n):
        a, b = map(int,input().split())
        ranks.append((a,b))
    ranks.sort(key=lambda x : x[0])
    count = 1
    last = ranks[0][1]
    for i in range(1,n):
        if ranks[i][1] < last :
            count += 1
            last = ranks[i][1]
    print(count)