
def solution(citations):
    for i in range(max(citations)+1):
        cnt=0
        for j in citations:
            if j>=i:
                cnt=cnt+1
        if cnt==i:
            answer=cnt
            break
       
        else:
            answer=0
                   
    return answer
print(solution([3,0,6,1,5]))
