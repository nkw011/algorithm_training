import sys
input = sys.stdin.readline

n = int(input().rstrip())
count = -1
nums = [[] for _ in range(11)]
nums[0] = -1
find = False
for i in range(1,11):
    if i == 1:
        for num in range(0,10):
            nums[i].append(num)
            count +=1
            if count == n:
                find = True
                print(num)
                break
    else :
        for num in range(1,10):
            for before in nums[i-1]:
                if num > (before // 10 **(i-2)):
                    count += 1
                    if count == n:
                        print(num * 10**(i-1)+ before)
                        find = True
                        break
                    nums[i].append(num*10**(i-1) + before)
    if find :
        break
if not find:
    print(-1)