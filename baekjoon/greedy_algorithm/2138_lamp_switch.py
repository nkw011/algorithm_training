import sys
input = sys.stdin.readline

n = int(input().rstrip())
lamp1 = list(map(int,input().rstrip()))
lamp2 = list(map(int,input().rstrip()))

def change(lamp,index):
    if not lamp[index]:
        lamp[index] = 1
    else :
        lamp[index] = 0
        
def equal(m1,m2):
    for i in range(n):
        if m1[i] != m2[i]:
            return False
    return True

# 0번을 누른 경우
temp1 = lamp1[:]
change(temp1,0)
change(temp1,1)
count1 = 1
for i in range(1,n):
    if temp1[i-1] != lamp2[i-1]:
        if i == n-1:
            change(temp1,i-1)
            change(temp1,i)
            count1 += 1
        else:
            change(temp1,i-1)
            change(temp1,i)
            change(temp1,i+1)
            count1 +=1
# 0번을 누르지 않은 경우
temp2 = lamp1[:]
count2 = 0
for i in range(1,n):
    if temp2[i-1] != lamp2[i-1]:
        if i == n-1:
            change(temp2,i-1)
            change(temp2,i)
            count2 +=1
        else:
            change(temp2,i-1)
            change(temp2,i)
            change(temp2,i+1)
            count2 +=1
            
if equal(temp1,lamp2) and equal(temp2,lamp2):
    print(min(count1,count2))
elif equal(temp1,lamp2):
    print(count1)
elif equal(temp2,lamp2):
    print(count2)
else :
    print(-1)