import sys
input = sys.stdin.readline

n = int(input().rstrip())
numbers = list(map(int,input().split()))
order = []

for i in range(n,0,-1):
    if numbers[i-1] == 0 :
        #퀵 정렬 만드는 방법을 이용하였다.
        nums1 = [x for x in order if x > i]
        nums2 = [x for x in order if x < i]
        order = nums2 + [i] + nums1
    else:
        # 어차피 자기보다 작은 것들은 카운트가 안되므로 그냥 j 값을 계속 올리는 방법을 사용해도된다.
        result = numbers[i-1]
        count = 0
        j = 0
        while j < len(order):
            if order[j] > i :
                count += 1
            if result == count:
                break
            j += 1
        order = order[:j+1] + [i] + order[j+1:]
        
for num in order:
    print(num,end=" ")