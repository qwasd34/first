def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i] in phone_book[i+1]:
            return print("false")
    return print("true")

ph=["119","893849","119349"]
solution(ph)
