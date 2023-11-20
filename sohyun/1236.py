N, M = map(int, input().split())
lst = []

for _ in range(N):
    temp_str = str(input())
    lst.append(temp_str)

# print(lst)
# print(lst[0][0])
# print(lst[0][1])
row = [0] * M
col = [0] * N
for i in range(N):
    for j in range(M):
        if lst[i][j] == 'X':
            row[j] = 1
            col[i] = 1

row_cnt = 0
col_cnt = 0
for r in row:
    if r == 0:
        row_cnt += 1

for c in col:
    if c == 0 :
        col_cnt += 1

cnt = 0
if row_cnt > col_cnt:
    cnt = row_cnt
elif row_cnt < col_cnt:
    cnt = col_cnt
else:
    cnt = row_cnt

print(cnt)
