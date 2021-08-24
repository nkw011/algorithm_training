import sys
input = sys.stdin.readline

n = int(input().rstrip())
nums1 = list(map(int,input().split()))
nums2 = list(map(int,input().split()))

nums1.sort(reverse=True)
nums2.sort()
result = 0
for i in range(n):
    result += (nums1[i] * nums2[i])
print(result)