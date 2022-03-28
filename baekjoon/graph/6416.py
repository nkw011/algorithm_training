import sys
from collections import defaultdict
def input(): return sys.stdin.readline().rstrip()

# 문제에서 설명하는 트리 조건
# 1. 노드가 0개
# 2. 노드가 1개 이상인 경우
#   2.1. 루트가 1개 존재
#   2.2. 루트를 제외한 모든 노드는 반드시 단 하나의 들어오는 간선이 존재한다
#   2.3. 루트에서 다른 노드로 가는 경우는 반드시 존재하며 유일하다

# 변수 설명
# in_degree[k]: k-노드로 들어가는 간선의 수
# out_degree[k]: k-노드에서 나가는 간선의 수
# input_end: 입력 끝, tree_end: 트리 끝, tree_num: 몇 번째 트리인지 표시

# 문제 풀이
# 1. 노드를 입력받으면서 각 노드로 들어오는 간선의 갯수가 몇 개인지, 각 노드로 부터 나가는 간선의 갯수가 몇 개인지 체크
# 2. in_degree, out_degree의 원소가 모두 없으면 노드가 없다는 뜻이므로 True
# 3. in_degree, out_degree의 원소가 1개 이상 존재하면
#   3.1. 각 노드로 들어오는 간선의 갯수가 1보다 큰 지 체크
#       1) 큰 게 있으면 False
#   3.2. 루트 노드가 1개 존재하는지 체크 -> (전체 노드 갯수 - out_degree의 원소 갯수) == 1
#       1) 1이면 True
#       2) 1이 아니면 False

in_degree,out_degree = defaultdict(int), defaultdict(int)
input_end, tree_end = False, False
tree_num = 1
while True:
    nodes = list(map(int,input().split()))
    for i in range(0,len(nodes),2):
        if nodes[i] == 0: 
            tree_end = True
            break
        if nodes[i] == -1:
            input_end = True
            break
        in_degree[nodes[i+1]] += 1
        out_degree[nodes[i]] += 1
    if tree_end:
        if len(out_degree) == 0 and len(in_degree) == 0:
            print(f"Case {tree_num} is a tree.")
            tree_num += 1
            tree_end = False
        else:
            is_tree,has_root = True, False
            for k in in_degree:
                if in_degree[k] > 1: is_tree = False
            if len(out_degree.keys() | in_degree.keys()) - len(in_degree.keys()) == 1:
                has_root = True
            if has_root and is_tree: print(f"Case {tree_num} is a tree.")
            else: print(f"Case {tree_num} is not a tree.")
            in_degree.clear()
            out_degree.clear()
            tree_num += 1
            tree_end = False
    if input_end:
        break
