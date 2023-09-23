# 시간 초과...
# def Fibo(n):
#     if (n == 0):
#         return 0
#     elif (n ==1):
#         return 1
#     else:
#         return Fibo(n-1) + Fibo(n-2)
    
def Fibo1(n):
    fibo_list = [0,1]
    for idx in range(2, n+1):
        fibo_list.append(fibo_list[idx-1] + fibo_list[idx-2])
    
    return fibo_list[n]



n = int(input())

print(Fibo1(n))

