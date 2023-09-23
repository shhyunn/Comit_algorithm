
T = int(input())

def gcd(a,b):
    while b != 0:
        a,b = b, a%b
    return a


def lcm(a,b):
    lcm_num = a*b // gcd(a,b)
    return lcm_num

for _ in range(T):
    A, B = map(int, input().split( ))
    print(lcm(A,B))




