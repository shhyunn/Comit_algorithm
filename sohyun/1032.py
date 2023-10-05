N = int(input())

string_list = []

for _ in range(N):
    temp_str = str(input())
    string_list.append(temp_str)

letter = ''
for i in range(len(string_list[0])):
    alpha = string_list[0][i]
    for j in range(1,N):
        if alpha != string_list[j][i]:
            alpha = '?'
            break
    
    letter += alpha

print(letter)
        