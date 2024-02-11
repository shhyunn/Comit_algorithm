import sys
input = sys.stdin.readline
N = int(input())

temp = 0
num = 666

# def find(n,i):
#     if n[i] == "6" and n[i+1] == "6" and n[i+2] == "6":
#         return True
#     return False

# def check(n):
#      mask=False
#      for i in range(len(n)-2):
#         if find(n,i):
#             mask=True
#             return mask
        
#      return mask


while True:
    strr = str(num)
    if "666" in strr:
        temp += 1
    if N == temp:
        break
    num += 1

print(num)

'''브루트 포스 알고리즘'''