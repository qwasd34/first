
def solution(numbers):
    answer=''
    a=[]
    numbers=list(map(str,numbers))
    a=sorted(numbers,key=lambda x: (x[0],x[1%len(x)], x[2%len(x)],x[3%len(x)]),reverse=True)
    print(a)
    for i in a:
        answer=answer+i
    if int(answer)==0:
        answer="0"
    return answer
  
print(solution([723,37,30,6,22]))
