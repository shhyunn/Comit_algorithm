letters = []
length =[]
i = 0
k = 0
m = 0
n = 0
res = []
while i < 5:
    var = str(input())
    letters.append(var)
    length.append(len(var))
    i+=1

longest = length[0]
while k < 4:
    if length[k+1] > longest:
        longest = length[k+1]
    k+=1

while m < longest:
    n = 0
    while n < 5:
        if len(letters[n]) > m:
            res.append(letters[n][m])
        n+=1
    m+=1

for x in res:
    print(x, end='')