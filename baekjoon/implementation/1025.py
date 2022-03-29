import sys
from functools import reduce
def input(): return sys.stdin.readline().rstrip()

# 문제에서 주어진 조건을 면밀히 분석해서 계속해서 틀리는 일이 없도록 주의하자!
# 코드를 더 단순하고 가독성이 좋게 짤 수는 없는지 고려하자! (문제를 다 풀고 어떻게 바꿀지 생각해보기)

# 3가지 조건을 모두 고려하지 않으면 오류가 나온다
# 1) 행, 열에 각각 적용되는 공차가 달라도 된다.
# 2) 총 몇 개의 숫자를 반영해 숫자를 만들 것인가
# 3) 숫자를 만드는 8가지 방법
#    -> 단순하게 생각해서 더하는 것만 생각하면 3가지 인데 등차수열은 공차가 음수여도 되므로 빼는 것까지 생각하면 총 8가지이다.

def make_number(x1,x2):
    return x1*10 + x2

def check(r,c):
    nums = []
    for r_d in range(-max_d-1,max_d+1):
        for c_d in range(-max_d-1,max_d+1):
            for cnt in range(1,max(n,m)+1):
                num = [matrix[r+i*r_d][c+i*c_d] for i in range(cnt) if 0<= r+i*r_d < n and 0 <= c + i*c_d< m]
                if len(num) == cnt:
                    nums.append(reduce(make_number,num))
    result = -1
    for num in nums:
        if num in square_number and result < num:
            result = num
    return result

n,m = map(int,input().split())
matrix = [list(map(int,input())) for _ in range(n)]
square_number = set([ num**2 for num in range(0,100001)])

max_d = max(n,m)
result = -1
for i in range(n):
    for j in range(m):
        temp = check(i,j)
        if result < temp:
            result = temp
print(result)
