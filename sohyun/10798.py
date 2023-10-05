str_list = []
long = 0
for _ in range(5):
    temp = str(input())
    str_list.append(temp)

    if (len(temp) > long):
        long = len(temp)

for i in range(long):
    for word in str_list:
        if (i >= len(word)):
            continue
        print(word[i], end="")