import sys
input = sys.stdin.readline

nums = list(map(int,input().rstrip()))
length = len(nums)
alpha = [[0] * 27 for _ in range(length)]
if nums[0] == 0:
    print(0)
else :
    alpha[0][nums[0]] = 1
    for i in range(1,length):
        for j in range(1,27):
            if alpha[i-1][j] != 0:
                if 1 <= nums[i] <= 26:
                    alpha[i][nums[i]] += alpha[i-1][j]
                if 1 <= j *10 + nums[i] <= 26:
                    alpha[i][j*10+nums[i]] += alpha[i-1][j]
    print(sum(alpha[length-1]) %1000000)