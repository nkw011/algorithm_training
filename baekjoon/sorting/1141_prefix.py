import sys
input = sys.stdin.readline

n = int(input().rstrip())
words = [input().rstrip() for _ in range(n)]
words = sorted(words,key = lambda x:(len(x),x))
count = 0
prefix = []
for i in range(n):
    word = words[i]
    len1 = len(word)
    possible = True
    for j in range(len(prefix)):
        len2 = len(prefix[j])
        if prefix[j][:len1] == word or word[:len2] == prefix[j]:
            possible = False
    if possible:
        prefix.append(word)
        count += 1
        
print(count)