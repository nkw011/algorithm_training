# 풀이 및 해설1: https://velog.io/@nkw011/baekjoon-2357
# 풀이 및 해설2: https://nkw011.github.io/baekjoon/baekjoon-2357/

import sys
def input(): return sys.stdin.readline().rstrip()

class SegmentTree:
    def __init__(self,n,array):
        self.n = n
        self.array = array
        self.min_tree = [0] * (4*n)
        self.max_tree = [0] * (4*n)
        self.INT_MAX = int(1e15)
        self.INT_MIN = 0

        self.min_init(0,n-1,1)
        self.max_init(0,n-1,1)

    def min_init(self, left, right, idx):
        if left == right:
            self.min_tree[idx] = self.array[left]
            return self.min_tree[idx]
        mid = (left+right) // 2
        self.min_tree[idx] = min(self.min_init(left, mid, 2*idx),
                                 self.min_init(mid+1, right, 2*idx+1))
        return self.min_tree[idx]

    def max_init(self, left, right, idx):
        if left == right:
            self.max_tree[idx] = self.array[left]
            return self.max_tree[idx]
        mid = (left+right) // 2
        self.max_tree[idx] = max(self.max_init(left, mid, 2*idx),
                                 self.max_init(mid+1, right, 2*idx+1))
        return self.max_tree[idx]

    def min_query(self, left, right, idx, node_left, node_right):
        if node_left > right or node_right < left:
            return self.INT_MAX
        if left <= node_left and node_right <= right:
            return self.min_tree[idx]
        mid = (node_left+node_right) // 2
        return min(self.min_query(left, right, 2*idx, node_left, mid),
                   self.min_query(left, right, 2*idx+1, mid+1, node_right))

    def max_query(self, left, right, idx, node_left, node_right):
        if node_left > right or node_right < left:
            return self.INT_MIN
        if left <= node_left and node_right <= right:
            return self.max_tree[idx]
        mid = (node_left+node_right) // 2
        return max(self.max_query(left, right, 2*idx, node_left, mid),
                   self.max_query(left, right, 2*idx+1, mid+1, node_right))

    def find_min_max(self, left, right):
        return self.min_query(left, right, 1, 0, self.n-1), self.max_query(left,right, 1, 0, self.n-1)


n, m = map(int,input().split())
nums = [int(input()) for _ in range(n)]
segment_tree = SegmentTree(n, nums)
for _ in range(m):
    a, b = map(int, input().split())
    print(*segment_tree.find_min_max(a-1,b-1))
