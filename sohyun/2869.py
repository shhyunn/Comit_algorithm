A, B, V = map(int, input().split(' '))

# length = 0
# day = 0
# while (length < V):
#     day += 1 #1 #2 #3 #4
#     length += A #2 #3 #4 #5
#     if (length < V):
#         length -= B #1 #2 #3



#A만큼 오르고, B만큼 다시 내려가는데, 

# x = int (A / (A - B))

# res = (V - ((A-B) * x)) // (A - B) + 1 
# print(res)

day = (V - B) / (A - B)
if (day == int(day)):
    print(int(day))
else:
    print(int(day) + 1)
