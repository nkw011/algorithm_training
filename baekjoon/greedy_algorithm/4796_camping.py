import sys
input = sys.stdin.readline

loop = 1
while True:
    l,p,v = map(int,input().split())
    
    if l == 0 and p == 0 and v == 0 :
        break

    count = (v//p) * l 
    if v%p >= l:
        count += l
    else :
        # 나머지가 l보다 클 수가 있으니 이 점에 유의해야한다.
        # 조금만 더 생각해보면 가능했을 것 같은데..... 너무 생각을 안하는 편인 것 같다.
        # 틀렸다고 겁먹지 말고 차근차근하면 해결이 될 것같다. 문제 조건을 꼼꼼히 읽자...
        count += v%p
    print("Case {0}: {1}".format(loop,count))
    loop += 1