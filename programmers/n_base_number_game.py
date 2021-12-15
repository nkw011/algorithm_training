# https://programmers.co.kr/learn/courses/30/lessons/17687

base = {i:str(i) for i in range(10)}
for num,alpha in zip([10,11,12,13,14,15],'ABCDEF'):
    base[num] = alpha
    
def base_number(number,n):
    if number < n:
        return base[number]
    return base[number % n] + base_number(number // n,n)

def solution(n,t,m,p):
    string = ''
    # 길이 제한이 어디가지 인지 몰라서 100000으로 일단 잡았다.
    for num in range(100000):
        string += base_number(num,n)[::-1]
        if len(string) >= t*m:
            break
    return ("".join([string[i] for i in range(p-1,t*m,m)]))[:t]
