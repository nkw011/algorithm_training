import sys
input = sys.stdin.readline

n, l = map(int,input().split())
holes = list(map(int,input().split()))
# 테스트 케이스가 오름차순이라고 모든 케이스가 오름차순인 것은 아니다
# 조건에서 과연 오름차순인지 잘 확인하자
holes.sort()

length = 0
count = 0
result = 0

#뭔가 코드를 단축시킬 수 있으면 좋을텐데ㅐ.. 아직은 그럴 짬이 아닌가? 일단 푸는게 우선인가?
for i in range(n):
    # 첫 케이스와 첫 케이스가 아닌 걸로 나누기
    if i ==0:
        length += 1
    else :
        result = holes[i] - holes[i-1]
        
    # 테이프로 커버할 수 있는 지 확인 대신 마지막 케이스를 위해 따로 점검
    if i == n-1:
        if length + result <= l:
                count += 1
        else :
            count += 2
    else :
        if length + result <= l :
            length += result
        else:
            length = 1
            count += 1
        
print(count)