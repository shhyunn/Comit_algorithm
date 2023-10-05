start, end = map(int, input().split())

sum = 0
num_arr = []
temp_num = 1
exit = 0

while (exit == 0):
    for _ in range(temp_num):
        num_arr.append(temp_num)
        
        if (sum == end):
            exit = 1
            break

        sum += 1

    temp_num += 1

result = 0
for i in range(start-1, end):
    result += num_arr[i]

print(result)
