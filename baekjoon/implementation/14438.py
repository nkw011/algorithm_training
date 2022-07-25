# 풀이 및 해설1: https://velog.io/@nkw011/baekjoon-14438
# 풀이 및 해설2: https://nkw011.github.io/baekjoon/baekjoon-14438/

import sys
def input(): return sys.stdin.readline().rstrip()

class SegmentTree:
    def __init__(self, n, array):
        self.n = n
        self.array = array
        self.tree = [0] * (4*n)
        self.make_tree(0,n-1,1)

    def make_tree(self, left, right, idx):
        if left == right:
            self.tree[idx] = self.array[left]
            return self.tree[idx]
        mid = (left + right) // 2
        self.tree[idx] = min(self.make_tree(left,mid,2*idx),
                             self.make_tree(mid+1,right,2*idx+1))
        return self.tree[idx]

    def find_min(self, left, right, idx, node_left, node_right):
        if left > node_right or right < node_left:
            return int(1e12)
        if left <= node_left and node_right <= right:
            return self.tree[idx]
        mid = (node_left + node_right) // 2
        return min(self.find_min(left, right, 2*idx, node_left, mid),
                   self.find_min(left, right, 2*idx+1, mid+1, node_right))

    def update_value(self, index, new_value, node_left, node_right, node_idx):
        if index < node_left or index > node_right:
            return self.tree[node_idx]
        if node_left == node_right:
            self.tree[node_idx] = new_value
            return self.tree[node_idx]
        mid = (node_left + node_right) // 2
        self.tree[node_idx] = min(self.update_value(index, new_value, node_left, mid, 2*node_idx),
                                  self.update_value(index, new_value, mid+1, node_right, 2*node_idx+1))
        return self.tree[node_idx]

    def query(self, left, right):
        return self.find_min(left,right,1,0,self.n-1)

    def update(self, index, new_value):
        return self.update_value(index,new_value, 0, self.n-1, 1)

n = int(input())
nums = list(map(int, input().split()))
segment_tree = SegmentTree(n, nums)
for _ in range(int(input())):
    a, b, c = map(int, input().split())
    if a == 1:
        segment_tree.update(b-1,c)
    else:
        print(segment_tree.query(b-1,c-1))
