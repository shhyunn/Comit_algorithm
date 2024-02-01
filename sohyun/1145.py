a, b, c, d, e = map(int, input().split())

def gcd(a,b):
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a,b):
    return a* b // gcd(a,b)

lst = [a, b, c, d, e]
lst.sort()
res = lst[2]

res = []

#두 개의 최소 공배수
for i in range(3):
    for j in range(i+1,4):
        for k in range(j+1,5):
            temp = lcm(lst[i], lst[j])
            num = lcm(temp, lst[k])
            res.append(num)

print(min(res))