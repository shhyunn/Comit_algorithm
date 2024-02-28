import sys
sys.stdin = open("C:\\Users\\LG\\proj\\comit\\sohyun\\input.txt","r")
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    p = input().strip()
    n = int(input())
    lst_str = input().strip()
    if len(lst_str) >2:
        lst = list(map(int,lst_str[1:-1].split(",")))
    else:
        lst = []
    # print(lst)
    error = 0
    seq = 1 #순행
    # front = 0
    # back = -1

    for c in p:
        if c == "R":
            # lst.reverse()
            if seq == 1:
                seq = 0
            else:
                seq = 1

        else:
            if len(lst) == 0:
                error = 1
                break
            if seq == 1:
                lst.pop(0)

            if seq == 0:
                lst.pop()

    if error == 1:
        print("error")
    else:
        if seq == 0:
            lst.reverse()
        
        print("["+",".join(map(str,lst))+"]")


#첫번째 수 버리기
#seq = 1   