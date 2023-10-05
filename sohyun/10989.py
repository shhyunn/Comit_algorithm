#카운팅 정렬
import sys

N = int(sys.stdin.readline())
arr = [0] * 10001
# sorted_arr = []

for _ in range(N):
    num = int(sys.stdin.readline())
    arr[num] += 1


for i in range(len(arr)):
    for _ in range(arr[i]):
        print(i)
        # sorted_arr.append(i)

# for res in sorted_arr:
#     print(res)

#이진탐색 정렬
# def binary_insert(arr,num):
#     low = 0
#     high = len(arr)-1

#     while low <= high:
#         mid = (low + high) // 2
#         if arr[mid] < num:
#             low = mid + 1
        
#         else:
#             high = mid - 1
#     arr.insert(low,num)
#     return arr



# for _ in range(N):
#     num = int(input())
#     res_arr = binary_insert(arr,num)

# for res in res_arr:
#     print(res)

#퀵정렬
# def partition(A, left, right):
#     low = left + 1
#     high = right
#     pivot = A[left]
#     while (low <= high):
#         while low <= high and A[low] < pivot: low += 1
#         while high >= left and A[high] > pivot: high -=1

#         if low < high:
#             A[low], A[high] = A[high], A[low]
    
#     A[left], A[high] = A[high], A[left]
#     return high

# def quick_sort(A, left, right):
#     if left<right:
#         mid = partition(A, left, right)
#         quick_sort(A,left, mid-1)
#         quick_sort(A,mid+1, right)
#         return A



# for _ in range(N):
#     num = int(input())

#     lista.append(num)

# result_list = quick_sort(lista, 0, len(lista) - 1)
# for res in result_list:
#     print(res)

#삽입 정렬
# for _ in range(N):
#     num = int(input())
#     for i, target in enumerate(lista):
#         if num < target:
#             lista.insert(i, num)

# for i in range(len(lista)-1):
#     for j in range(i+1,len(lista)):
#         if lista[i] > lista[j]:
#             lista[i], lista[j] = lista[j], lista[i]


