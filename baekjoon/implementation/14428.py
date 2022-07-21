# 풀이 및 해설1: https://nkw011.github.io/baekjoon/baekjoon-14428/
# 풀이 및 해설2: https://velog.io/@nkw011/baekjoon-14428

import sys
def input(): return sys.stdin.readline().rstrip()

class SegmentTree:
    def __init__(self, n, array):
        self.n = n
        self.array = array
        self.tree = [0] * (4*n)
        self.make_tree(0,n-1,1)

    def make_tree(self, node_left, node_right, idx):
        if node_left == node_right:
            self.tree[idx] = (self.array[node_left], node_left)
            return self.tree[idx]
        mid = (node_left + node_right) // 2
        val1, array_idx1 = self.make_tree(node_left, mid, 2*idx)
        val2, array_idx2 = self.make_tree(mid+1,node_right, 2*idx+1)
        if val1 < val2:
            self.tree[idx] = (val1, array_idx1)
        elif val1 > val2:
            self.tree[idx] = (val2, array_idx2)
        else:
            array_idx = min(array_idx1, array_idx2)
            self.tree[idx] = (val1, array_idx)
        return self.tree[idx]

    def find_min_value(self, left, right, idx, node_left, node_right):
        if right < node_left or left > node_right:
            return int(1e10), 100001
        if left <= node_left and node_right <= right:
            return self.tree[idx]
        mid = (node_left + node_right) // 2
        val1, array_idx1 = self.find_min_value(left, right, 2*idx, node_left, mid)
        val2, array_idx2 = self.find_min_value(left, right, 2*idx+1, mid+1, node_right)
        if val1 < val2:
            return val1, array_idx1
        elif val1 > val2:
            return val2, array_idx2
        else:
            array_idx = min(array_idx1, array_idx2)
            return val1, array_idx

    def update(self, node_left, node_right, node_idx, index, new_value):
        if index < node_left or index > node_right:
            return self.tree[node_idx]
        if node_left == node_right:
            self.tree[node_idx] = new_value, index
            return self.tree[node_idx]
        mid = (node_left + node_right) // 2
        val1, array_idx1 = self.update(node_left, mid, 2*node_idx, index, new_value)
        val2, array_idx2 = self.update(mid+1, node_right, 2*node_idx+1, index, new_value)
        if val1 < val2:
            self.tree[node_idx] = (val1, array_idx1)
        elif val1 > val2:
            self.tree[node_idx] = (val2, array_idx2)
        else:
            array_idx = min(array_idx1, array_idx2)
            self.tree[node_idx] = (val1, array_idx)
        return self.tree[node_idx]

    def query(self, i, j):
        return self.find_min_value(i,j,1,0,self.n-1)

    def update_value(self, i, v):
        return self.update(0,self.n-1,1,i,v)

n = int(input())
nums = list(map(int,input().split()))
segment_tree = SegmentTree(n, nums)

for _ in range(int(input())):
    comm, a, b = map(int,input().split())
    if comm == 1:
        segment_tree.update_value(a-1,b)
    else:
        val, index = segment_tree.query(a-1,b-1)
        print(index+1)
