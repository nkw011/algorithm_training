# 1차 풀이 : 완전 탐색
# 그것을 포함시키냐 포함시키지 않느냐의 여부는 이진수를 만들어서 1이면 넣고 0이면 넣지 않는 것으로 표현 가능하다.
# (꼭 순열과 조합을 이용하는 방법만 있는 것은 아니다.)
# 따라서 경우의 수는 20!이 아닌 2^20가지 이다.
# 너무 한 가지 풀이만을 생각하지 말고 가볍게 여러가지 풀이를 생각할 수 있도록 노력하자

# import sys
# input = sys.stdin.readline

# def dfs(count,number):
#     global maxValue
#     if count == n:
#         health = 100
#         joy = 0
#         possible = True
#         for i in range(n):
#             if number[i] == 1:
#                 health -= L[i]
#                 joy += J[i]
#             if health <= 0:
#                 possible = False
#                 break
#         if possible:
#             maxValue = max(maxValue,joy)
#         return
#     else :
#         number.append(1)
#         dfs(count+1,number)
#         number.pop()
        
#         number.append(0)
#         dfs(count+1,number)
#         number.pop()
            
# n = int(input().rstrip())
# L = list(map(int,input().split()))
# J = list(map(int,input().split()))
# maxValue = 0

# dfs(0,[])
# print(maxValue)



# 2차 풀이 다이나믹 프로그래밍
# 완전 탐색으로 만든 것을 이용해 다이나믹 프로그래밍으로 변경하는 법을 알아내자...
# 일단 DP 자료형을 몇차원으로 만들 것인지에 대한 고민이 필요한 것 같다.
# i : 지금 인사하는 사람의 순번 / j: 체력으로 생각하는 것 같다...
# 한 번 내일 이렇게 풀어봐야지

import sys
input = sys.stdin.readline

n = int(input().rstrip())
L = list(map(int,input().split()))
J = list(map(int,input().split()))

