T = int(input())
str_list = []

for _ in range(T):
    temp_str = str(input())
    str_list.append(temp_str)

for temp_str in str_list:
    word_list = list(map(str, temp_str.split(' ')))

    for word in word_list:
        if (len(word) == 1):
            print(word + " ", end="")
            continue
        
        for j in range(len(word)):
            print(word[-1-j], end="")
        
        print(" ", end="")

    print("")
