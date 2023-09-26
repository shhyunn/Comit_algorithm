N = int(input())
i = 0
k = 1
l = 0
listall = []
while i < N:
    inp = str(input())
    listall.append(inp)
    i += 1

standard = list(listall[0])

while k < N:
    while l < len(standard):
        if standard[l] != listall[k][l]:
            standard[l] = '?'
        l += 1
    k += 1
    l = 0

res = ''.join(standard)
print(res)