def solution(budgets, M):
    budgets.sort()
    s,cnt=0,0
    n=len(budgets)
    if sum(budgets)<=M:
        answer=max(budgets)
    else:
        tmp=M//n
        for i in budgets:
            if i<=tmp:
                s=i+s
                cnt=cnt+1
            else:
                tmp=(M-s)//(n-cnt)
                if i<=tmp:
                    s=i+s
                    cnt=cnt+1
        answer=(M-s)//(n-cnt)            
        
    return answer
print(solution([50,50,50,50,100,100,120,120,200,240],1000))
print(solution([120,110,140,150],485))
