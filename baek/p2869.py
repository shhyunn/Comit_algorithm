A,B,V = (map(int,input().split()))
'''
location = 0
day = 0
while True:
    location += A
    day += 1
    if location >= V:
        print(day)
        break
    location -= B
'''

cal1 = V - A
cal2 = cal1 / (A-B)
if cal2 - int(cal2) == 0:
    res = int(cal2) + 1
else:
    res = int(cal2) + 2

print(res)