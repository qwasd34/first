def solution(num):
    cnt=0
    while True:
        if(num==1):
            break
       elif num%2==0:
            num=num/2
            cnt=cnt+1
        elif num%2==1:
            num=num*3+1
            cnt=cnt+1
            print('jj')
    return cnt
