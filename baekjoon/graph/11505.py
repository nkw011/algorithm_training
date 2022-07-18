# 풀이 및 해설1: https://velog.io/@nkw011/baekjoon-11505
# 풀이 및 해설2: https://nkw011.github.io/baekjoon/baekjoon-11505/

import sys
def input(): return sys.stdin.readline().rstrip()

class SegmentTree:
    def __init__(self, n, array):
        self.n = n
        self.array = array
        self.tree = [0] * (4*n)
        self.initialize(0,n-1,1)

    def initialize(self, left, right, idx):
        if left == right:
            self.tree[idx] = self.array[left] % 1000000007
            return self.tree[idx] % 1000000007
        mid = (left + right) // 2
        self.tree[idx] = (self.initialize(left, mid, 2*idx) * self.initialize(mid+1, right, 2*idx+1)) % 1000000007
        return self.tree[idx]

    def query(self, left, right, idx, node_left, node_right):
        if node_right < left or right < node_left:
            return 1
        if left <= node_left and node_right <= right:
            return self.tree[idx]
        mid = (node_left+node_right) // 2
        return( self.query(left, right, 2*idx, node_left, mid) * self.query(left, right, 2*idx+1, mid+1, node_right) ) % 1000000007

    def update(self, index, new_value, node_idx, node_left, node_right):
        # index가 node가 표현하는 구간에 속하지 않는 경우 먼저 종료하는 것이 필요하다.
        if index < node_left or index > node_right:
            return self.tree[node_idx]
        if node_left == node_right:
            self.tree[node_idx] = new_value % 1000000007
            return self.tree[node_idx] % 1000000007
        mid = (node_left+node_right) // 2
        self.tree[node_idx] = (self.update(index, new_value, 2*node_idx, node_left, mid) * self.update(index, new_value, 2*node_idx+1, mid+1, node_right)) % 1000000007
        return self.tree[node_idx]

    def find_prod(self, left, right):
        return self.query(left, right, 1, 0, self.n-1)

    def update_value(self, index, value):
        return self.update(index, value, 1, 0, self.n-1)

n, m, k = map(int,input().split())
nums = [int(input()) for _ in range(n)]
segment_tree = SegmentTree(n, nums)
for _ in range(m+k):
    a, b, c = map(int, input().split())
    if a == 1:
        segment_tree.update_value(b-1, c)
    else:
        print(segment_tree.find_prod(b-1,c-1))
