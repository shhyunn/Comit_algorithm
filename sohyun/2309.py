p1 = int(input())
p2 = int(input())
p3 = int(input())
p4 = int(input())
p5 = int(input())
p6 = int(input())
p7 = int(input())
p8 = int(input())
p9 = int(input())

person = [p1, p2, p3, p4, p5, p6, p7, p8, p9]
exceptFor = []

for n1 in range(9):
    for n2 in range(n1+1,9):
        exceptFor.append((n1,n2))

# print(len(exceptFor))

for length in range(len(exceptFor)):
   temp_list = [item for idx, item in enumerate(person) if idx not in exceptFor[length]]
   if (sum(temp_list) == 100):
       res = sorted(temp_list)
       break

for num in res:
    print(num)

        