import itertools
import math
def solution(numbers):
    answer=[]
    numbers=list(numbers)
    num=[]
    for i in range(len(numbers)):
        arr=[]
        arr=(list(map(''.join,itertools.permutations(numbers,len(numbers)-i))))
        num=num+arr
    num=list(set(map(int,num)))
   # num=list(set(num))  #중복된값 제거
    '''for i in num:
        n=list(range(2,i+1))
        result=[k for k in n if i%k==0]
        if len(result)==1:
            answer=answer+1'''
    for i in num:
        cnt=0
        sqrt=int(math.sqrt(i))
        if i!=0 and i!=1:
            for j in range(2,sqrt+1):
                if i%j==0:
                    cnt+=1
            if cnt==0:
                answer.append(i)
    return len(answer)

print(solution("17"))
