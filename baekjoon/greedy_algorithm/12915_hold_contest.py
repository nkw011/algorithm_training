import sys
input = sys.stdin.readline

e,em,m,mh,h = map(int,input().split())
count = 0

while True:
    e_pass, m_pass, h_pass = False,False,False
    if e > 0:
        e -= 1
        e_pass = True
    else :
        if em >0:
            em -= 1
            e_pass = True
    if h > 0:
        h -= 1
        h_pass = True
    else :
        if mh > 0:
            mh -= 1
            h_pass = True
            
    if m > 0:
        m -= 1
        m_pass = True
    else :
        if em > 0 and em >= mh:
            em -= 1
            m_pass = True
        elif mh > 0 and mh > em:
            mh -= 1
            m_pass = True
            
    if e_pass and m_pass and h_pass:
        count += 1
    else :
        break
print(count)