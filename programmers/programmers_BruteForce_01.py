from itertools import cycle

def solution(num):
    cnt=[-1,0,0,0]
    answers=[]
    soopo1=[1,2,3,4,5]
    soopo2=[2,1,2,3,2,4,2,5]
    soopo3=[3,3,1,1,2,2,4,4,5,5]
    s1=cycle(soopo1)
    s2=cycle(soopo2)
    s3=cycle(soopo3)
    for i in num:
        if i==next(s1):
            cnt[1]=cnt[1]+1
        if i== next(s2):
            cnt[2]=cnt[2]+1
        if i==next(s3):
            cnt[3]=cnt[3]+1
    m=max(cnt)
    answers=[k for k, j in enumerate(cnt) if j==m]
    return answers
print(solution([0,0,0,0,0,0]))
