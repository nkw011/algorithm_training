import sys
def input(): return sys.stdin.readline().rstrip()

# 아이디어: 멀리 있는 위치일수록 1번만 방문하는 것이 좋다
# 문제풀이
# 1. 책의 위치를 입력받은 이후 음수 위치와 양수 위치로 구분한다
# 2. 양수 위치에서 가장 큰 값부터 m개씩 끊어서 move 배열에 담는다
# 3. 음수 위치에서 가장 작은 값부터 m개씩 끊어서 move 배열에 담는다.
# 4. 가장 먼 위치를 알아내기 위해 move 배열을 절댓값을 기준으로 정렬
# 5. 가장 먼 위치는 1번만 방문하고 나머지 위치는 왕복한 거리를 출력


n,m = map(int,input().split())
items = sorted(list(map(int,input().split())))
pos = [num for num in items if num > 0]
neg = [num for num in items if num < 0]
move = []
for i in range(-1,-len(pos)-1,-m):
    move.append(pos[i])
for i in range(0,len(neg),m):
    move.append(-neg[i])
move.sort(key= lambda x: abs(x))
print(move[-1] + sum(move[:-1]) * 2)
