import sys
from collections import deque

sys.stdin = open("C:\\Users\\LG\\proj\\comit\\sohyun\\input.txt","r")
input = sys.stdin.readline

#노드, 왼쪽노드, 오른쪽 노드
N = int(input())
# graph = {chr(key):[] for key in range(65,66+N)}
graph = {}

for _ in range(N):
    a,b,c = input().strip().split()
    graph[a] = [b,c]

def preorder(n):
    global res1
    if n == ".":
        return

    res1 += n
    preorder(graph[n][0])
    preorder(graph[n][1])

def centerorder(n):
    global res2
    if n == ".":
        return
    
    centerorder(graph[n][0])
    res2 += n
    centerorder(graph[n][1])

def postorder(n):
    global res3
    if n == ".":
        return
    
    postorder(graph[n][0])
    postorder(graph[n][1])
    res3 += n

res1 = ""
res2 = ""
res3 = ""

preorder("A")
centerorder("A")
postorder("A")

print(res1)
print(res2)
print(res3)