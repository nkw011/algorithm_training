import sys
input = sys.stdin.readline

n = int(input().rstrip())
a,b = map(int,input().split())
c = int(input().rstrip())
topings = [int(input().rstrip()) for _ in range(n)]
topings.sort(reverse=True)

# 토핑을 아예 선택하지 않는 경우도 생각해야한다....
# 정답이라는 확신이 드는 순간 문제를 다시 읽고 조건을 빼먹은 것이 없는 지 확인을 해보자!!! -> 이게 진정 중요한 습관이다.
calory = c
money = a
maxValue = calory // money

for i in range(n):
    calory += topings[i]
    money += b
    maxValue = max(maxValue,calory // money)
    
print(maxValue)