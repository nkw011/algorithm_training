# 풀이 및 해설1: https://velog.io/@nkw011/baekjoon-14725
# 풀이 및 해설2: https://nkw011.github.io/baekjoon/baekjoon-14725/

import sys
def input(): return sys.stdin.readline().rstrip()

class Node:
    def __init__(self, key):
        self.key = key
        self.children = {}

class Trie:
    def __init__(self):
        self.head = Node(None)
    def insert(self, string):
        curr_node = self.head
        for c in string:
            if c not in curr_node.children:
                curr_node.children[c] = Node(c)
            curr_node = curr_node.children[c]

def print_node(now:Node, i:int, isHead=False):
    '''
    문제에서 요구하는 형식으로 출력하는 함수
    '''
    if not isHead:
        print("--"*i + now.key)
    sorted_keys = sorted(now.children.keys())
    for child in sorted_keys:
        print_node(now.children[child], i+1)

n = int(input())
trie = Trie()
for _ in range(n):
    path = input().split()[1:]
    trie.insert(path)
print_node(trie.head,-1,True)
