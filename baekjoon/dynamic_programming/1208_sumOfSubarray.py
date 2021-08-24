# 음수 index가 필요할 때 map을 사용하는 방법 너무 좋은 것 같다.
# 조합 알고리즘을 사용할 때 사이즈가 너무 크다면
# 반으로 줄이는 방법도 생각하면 좋은 것 같다.

import sys
def input(): return sys.stdin.readline().rstrip()


def dfs1(i, plus, limit, count):
    if i == limit:
        # 어차피 0에 대한 것은 1번만 나오기 때문에 s가 0이라면 answer - 1을 해주면 된다.
        if n != 0 and count == 0:
            return
        if plus < 0:
            sum2[-plus] += 1
        else:
            sum1[plus] += 1
        return
    dfs1(i+1, plus+nums[i], limit, count+1)
    dfs1(i+1, plus, limit, count)


def dfs2(i, plus, limit, count):
    if i == limit:
        if count == 0:
            return
        if plus < 0:
            sum4[-plus] += 1
        else:
            sum3[plus] += 1
        return
    dfs2(i+1, plus+nums[i], limit, count+1)
    dfs2(i+1, plus, limit, count)


n, s = map(int, input().split())
nums = list(map(int, input().split()))
total, ng, ps = 0, 0, 0
for i in range(n):
    if nums[i] < 0:
        ng += nums[i]
    else:
        ps += nums[i]

# s가 total 보다 크다는 것을 간과하였다.
total = abs(ng) + abs(s) if abs(ng) > ps else ps + abs(s)

sum1 = [0] * (total+1)
sum2 = [0] * (total+1)
# 이 부분은 굳이 만들지 않았어도 되었다.
# 왜냐면 s- rightSum이 left에 존재하는 지 바로바로 체크하면 되기 때문이다. (dfs2에서)
sum3 = [0] * (total + 1)
sum4 = [0] * (total + 1)

dfs1(0, 0, n//2, 0)
dfs2(n//2, 0, n, 0)

cnt = 0
if s >= 0:
    if sum1[s]:
        cnt += sum1[s]
    if sum3[s]:
        cnt += sum3[s]
else:
    if sum2[-s]:
        cnt += sum2[-s]
    if sum4[-s]:
        cnt += sum4[-s]

# 총 2번만 하면 될 것 같다.
for i in range(total+1):
    if sum1[i]:
        if s-i >= 0:
            cnt += sum1[i] * sum3[s-i]
        else:
            cnt += sum1[i] * sum4[i-s]
    if sum2[i]:
        if s + i >= 0:
            cnt += sum2[i] * sum3[s+i]
        else:
            # 이곳을 sum4가 아니라 sum3라고 적어서 틀렸습니다.
            cnt += sum2[i] * sum4[-i-s]

print(cnt)
