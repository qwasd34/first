import queue
from itertools import cycle
def solution(n, times):
    person=[]
    ti=[]
    t=0
    tl=len(times)
    for i in times:
        ti.append(i)
        t=t+i
        n=n-1
    print(n)
    print(t)
   
    for i in range(n):
        for j in range(tl):
            ti[j]=ti[j]+ti[j]
        t=t+min(ti)
        

    return t
print(solution(6,[7,10]))
