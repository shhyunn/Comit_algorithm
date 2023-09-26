T = int(input())
list1 = []
listres = []
i = 0
k = 0
while i < T:
    sentence = str(input())
    list1 = list(sentence.split(' '))
    while k < len(list1):
        word = list1[k]
        new_word = str(word[::-1])
        list1[k] = new_word
        k += 1
    res = ' '.join(list1)
    listres.append(res)
    k = 0
    i += 1

for n in range(len(listres)):
    print(listres[n])