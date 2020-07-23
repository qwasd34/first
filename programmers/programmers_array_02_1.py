import itertools 
def solution(numbers):
    answer=''
    numbers=list(map(str,numbers))
    num=list(map(''.join,itertools.permutations(numbers)))
    print(num)
    num=list(map(int,num))
    answer=max(num)
    answer=str(answer)
    return answer

print(solution([3,30,34,9,5]))
