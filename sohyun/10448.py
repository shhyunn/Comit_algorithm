
Tn = []

temp = 0
num = 1
while temp < 1000:
    temp += num
    Tn.append(temp)
    num += 1

T = int(input())

for i in range(T):
    N = int(input())
    result = 0
    end = 0
    for k in Tn:
        for m in Tn:
            for l in Tn:
                if N == (k + m + l):
                    result = 1
                    end = 1
                    break
            
            if end == 1:
                break
        
        if end == 1:
            break
        
    print("%d"%result)
