import sys
input = sys.stdin.readline

l,r = input().split()

if len(l) == len(r):
    count = 0
    for i in range(len(l)):
        if l[i] == r[i]:
            if l[i] =='8':
                count += 1
        else :
            break
    print(count)
else :
    print(0)