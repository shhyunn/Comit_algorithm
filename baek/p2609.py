import math
A,B = (map(int,input().split()))
cal1 = math.gcd(A,B)
cal2 = math.lcm(A,B)
print(cal1)
print(cal2)