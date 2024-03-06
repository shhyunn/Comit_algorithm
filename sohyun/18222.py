import sys,math
input = sys.stdin.readline

#x : 0으로 시작, 0을 1로, 1울 0으로 바꿈 x + x',x의 k번째에는 무슨 숫자가 올까?
k = int(input())
def div(x):
    temp = 1
    while True:
        temp *= 2
        if temp >= x:
            x = temp//2
            break
    return x

def find(x):
    if x == 1:
        return 0
    if x == 2:
        return 1
    
    return 1 - find(x-div(x))

print(find(k))