import sys
def input(): return sys.stdin.readline().rstrip()
# 방법
# 1. 입구에서 들어오는 순서대로 차 이름을 기록한다
#    예시) 첫번째로 들어오는 차 -> '1:차 이름'
# 2. 출구부터 나가는 차를 순서대로 순위를 기록한다
#    예시) 첫번째로 나가는 차 -> '차 이름:1'
# 3. 입구에서 첫번째로 들어간 차부터 순위를 살핀다
#    자신의 앞 차보다 나간 순서가 빠르면 추월

n = int(input())
in_cars = {i+1: input() for i in range(n)}
out_cars = {input(): i+1 for i in range(n)}

cnt = 0
# 입구에서 첫번째로 들어간 차의 나간 순서를 기록
# pre_rank: 앞 차 나간 순서 기록
pre_rank = out_cars[in_cars[1]]
for rank in in_cars:
    # 만약 앞 차 순위보다 낮은 경우 추월
    # 순서가 바뀌었기 때문에 pre_rank로 갱신하지 않는다
    if out_cars[in_cars[rank]] < pre_rank:
        cnt += 1
    # 앞 차가 나간순서보다 뒤에 나간 경우
    # pre_rank 갱신
    else:
        pre_rank = out_cars[in_cars[rank]]
print(cnt)
