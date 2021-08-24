import sys
input = sys.stdin.readline

n = int(input().rstrip())
people =[]
for i in range(n):
    person = list(input().split())
    age, name = int(person[0]), person[1]
    people.append((i,age,name))
    
people.sort(key=lambda x: (x[1],x[0]))

for person in people:
    print(person[1],person[2])