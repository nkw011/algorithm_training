import sys
sys.setrecursionlimit(150000)
def input(): return sys.stdin.readline().rstrip()

# tree: dictionary로 구성
# 1. 보통 이진 트리는 array를 이용해 일반적으로 구성하나 depth를 먼저 알아내야한다고 생각해 dictionary로 구성
# 2. IndexError를 피한다는 장점도 존재

# 이진 트리 구성: 인덱스를 이용해 각 트리의 노드에 접근한다.
# root 인덱스: 0
# 현재 노드의 인덱스를 idx라 할 때
# 1. 왼쪽 자식 노드: 2 * idx + 1
# 2. 오른쪽 자식 노드: 2 * idx + 2

# pre_order를 통한 트리 만들기
# 0. 첫번째 노드는 루트 노드 -> 인덱스 0으로 설정
# 그 다음 노드 부터
#    1. 이전 노드 보다 작으면 이전 노드의 왼쪽 자식 노드로 인덱스 설정
#    2. 이전 노드 보다 크면 지금까지 구성된 트리 노드 중에서 자기 자신보다 작은 노드 중 제일 큰 노드(부모 노드)를 찾아
#       그 노드의 오른쪽 자식 노드로 인덱스 설정

# post_order 순회
# 1. 왼쪽 자식 노드 탐색
# 2. 오른쪽 자식 노드 탐색
# 3. 부모 노드 출력


def post_order(idx):
    if idx * 2 + 1 in idx2node:
        post_order(idx*2+1)
    if idx*2 + 2 in idx2node:
        post_order(idx*2+2)
    print(idx2node[idx])


preorder = []
while True:
    try:
        preorder.append(int(input()))
    except:
        break

idx2node, node2idx = {}, {}
idx2node[0], node2idx[preorder[0]] = preorder[0], 0
for i in range(1, len(preorder)):
    if preorder[i-1] > preorder[i]:
        idx2node[node2idx[preorder[i-1]] * 2 + 1] = preorder[i]
        node2idx[preorder[i]] = node2idx[preorder[i-1]] * 2 + 1
    if preorder[i-1] < preorder[i]:
        node = 0
        for k in node2idx:
            if k < preorder[i] and node < k:
                node = k
        idx2node[node2idx[node]*2 + 2] = preorder[i]
        node2idx[preorder[i]] = node2idx[node]*2 + 2
post_order(0)
