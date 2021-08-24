import sys
input = sys.stdin.readline
sys.setrecursionlimit(30000)

def palindrome(string,left,right,check):
    if check >= 2 :
        return 2
    if left >= right:
        return check
    else:
        if string[left] == string[right]:
            return palindrome(string,left+1,right-1,check)
        else:
            a = int(1e9)
            b = int(1e9)
            if string[left] != string[right-1] and string[left+1] != string[right]:
                return 2
            if string[left+1] == string[right]:
                a = palindrome(string,left+1,right,check+1)
            if string[left] == string[right-1]:
                b = palindrome(string,left,right-1,check+1)
            return a if a < b else b

T = int(input().rstrip())
for loop in range(T):
    s = input().rstrip()
    check = palindrome(s,0,len(s)-1,0)
    print(check)