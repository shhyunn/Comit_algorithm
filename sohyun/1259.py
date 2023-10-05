while True:
    num = int(input())
    if (num == 0):
        break
    
    str_num = str(num)
    correct = 1

    for i in range(len(str_num)//2):
        if (str_num[i] == str_num[-1-i]):
            continue
        else:
            correct = 0
            print("no")
            break
    
    if (correct == 1):
        print("yes")
