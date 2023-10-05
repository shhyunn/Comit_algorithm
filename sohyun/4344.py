C = int(input())
for _ in range(C):
    list1 = list(map(int, input().split(' ')))
    num = list1[0]

    avg = sum(list1[1:]) / num
    
    res_list = [score for score in list1[1:] if score > avg]
    rate = (len(res_list)/list1[0]) * 100
    print("%.3f%%"%rate)