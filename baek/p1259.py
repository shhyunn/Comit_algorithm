list1 = []
i = 0
while True:
    a = str(input())
    if a == '0':
        break
    else:
        list1.append(a)

while i < len(list1):
    num1 = list1[i]
    num2 = str(num1[::-1])
    if num1 == num2:
        print("yes")
    else:
        print("no")
    i += 1
