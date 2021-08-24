import sys
input = sys.stdin.readline

e,s,m = map(int,input().split())
a,b,c = 1,1,1
count = 1
while a != e or b!= s or c != m:
    if a == 15:
        a = 1
    else :
         a += 1
            
    if b == 28:
        b = 1
    else :
        b += 1
        
    if c == 19:
        c = 1
    else :
        c += 1
    count += 1
print(count)