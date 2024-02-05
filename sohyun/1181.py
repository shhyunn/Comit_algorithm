N = int(input())
word_lst = {key:[] for key in range(1,51)}
for _ in range(N):
    word = str(input())
    th = len(word)
    word_lst[th].append(word)

for i in range(1,51):
    if len(word_lst[i])>=1:
        temp_lst = list(set(word_lst[i]))
        temp_lst.sort()

        for res in temp_lst:
            print(res)