# union-find를 이용하여 문제를 풀 시, 부모 노드를 찾을 때 무조건 findParent를 사용하자... 이것때문에 2시간 행복 코딩...
# 처음으로 테스트 코드를 만들어서 내 코드를 검증해보았다.. (뭔가 조금 뿌듯하다) -> 이로 인해 뭔가 새로 깨달은 것도 있는 것 같다.

import sys
input = lambda : sys.stdin.readline()

def findParent(x):
    if parent[x] != x:
        parent[x] = findParent(parent[x])
    return parent[x]

def union(a,b):
    a = findParent(a)
    b = findParent(b)
    if a < b:
        parent[b] = a
    else :
        parent[a] = b

n,m = map(int,input().split())
know = list(map(int,input().split()))
parent = [i for i in range(n+1)]
party = []
result = 0

for _ in range(m):
    nums = list(map(int,input().split()))
    leng = nums[0]
    for i in range(leng-1):
        if findParent(nums[i+1]) != findParent(nums[i+2]):
            union(nums[i+1],nums[i+2])
    party.append(nums[1:])
    
root = set()
for num in know[1:] :
    root.add(findParent(num))
    
for p in party:
    possible = True
    for num in p:
        if findParent(num) in root:
            possible = False
            root.add(num)
    if possible:
        result += 1
print(result)


##################################################################################################################################
##################################################################################################################################
##################################################################################################################################

### 아래는 테스트 코드 ######### 아래는 테스트 코드 ######### 아래는 테스트 코드 ######### 아래는 테스트 코드 ######### 아래는 테스트 코드 ####

import random
    
def findParent(parent,x):
    if parent[x] != x:
        parent[x] = findParent(parent,parent[x])
    return parent[x]

def union(parent,a,b):
    a = findParent(parent,a)
    b = findParent(parent,b)
    if a < b:
        parent[b] = a
    else :
        parent[a] = b

def myResult(n,m,know,parties):
    parent = [i for i in range(n+1)]
    result = 0
    party= []
    
    for i in range(m):
        nums = parties[i]
        leng = nums[0]
        for i in range(leng-1):
            if findParent(parent,nums[i+1]) != findParent(parent,nums[i+2]):
                union(parent,nums[i+1],nums[i+2])
        party.append(nums[1:])
        
    root = set()
    for num in know[1:] :
        root.add(findParent(parent,num))
        
    for p in party:
        possible = True
        for num in p:
            if findParent(parent,num) in root:
                possible = False
                root.add(num)
        if possible:
            result += 1
    return result
    
# 정답 코드는 블로그에 나와있는 것을 참고했다.
def answer(n,m,knows,parties):
    cnt_party = m
    witness_set = set(knows[1:])
    party_list = []
    possible_list = []
    for i in range(cnt_party):
        party_list.append(set(parties[i][1:]))
        possible_list.append(1)
    for _ in range(cnt_party):
        for i, party in enumerate(party_list):
            if witness_set.intersection(party):
                possible_list[i] = 0
                witness_set = witness_set.union(party)
    return sum(possible_list)
    
def test():
    while True:
        n = random.randrange(1,10)
        m = random.randrange(1,n+1)
        true = random.randrange(0,n+1)
        tr = [true]
        trues = set()
        for _ in range(true):
            tnum = random.randrange(1,n+1)
            while tnum in trues:
                tnum = random.randrange(1,n+1)
            trues.add(tnum)
        tr.extend(list(trues))
        
        edge = []
        for _ in range(m):
            te = []
            nums = set()
            ns = random.randrange(1,n+1)
            for _ in range(ns):
                num = random.randrange(1,n+1)
                while num in nums:
                    num = random.randrange(1,n+1)
                nums.add(num)
            te.append(ns)
            te.extend(list(nums))
            edge.append(te[:])
            
        ans = answer(n,m,tr,edge)
        n1 = myResult(n,m,tr,edge)
            
        # 1분 정도 해보고 반례가 나오지 않을 때는 정답이라 간주하고 제출하였다.
        if n1 != ans:
            print("n,m:",n,m)
            print("trues:",tr)
            print("tc: ",edge)
            print("myResult:",n1)
            print("answer:",ans)
            break
        
test()