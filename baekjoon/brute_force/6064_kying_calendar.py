import sys
input = sys.stdin.readline

def binarySearch(array,item):
    left = 0
    right = len(array) -1
    while left <= right:
        mid = (left+right) // 2
        if array[mid] == item:
            return mid
        elif array[mid] < item:
            left = mid +1
        else:
            right = mid - 1
    return -1

def gcd(a,b):
    while b!=0:
        r = a %b
        a = b
        b = r
    return a

def lcm (a,b):
    return a * b // gcd(a,b)

def findYear(m,n,x,y):
    number = lcm(m,n)
    find1 = [ num1 for num1 in range(x,number+1,m)]
    find2 = [ num2 for num2 in range(y,number+1,n)]
    
    for find in find1:
        if binarySearch(find2,find) != -1:
            return find
    return -1


T = int(input().rstrip())
for _ in range(T):
    m,n,x,y = map(int,input().split())
    print(findYear(m,n,x,y))