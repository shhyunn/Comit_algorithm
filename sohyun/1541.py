import sys
input = sys.stdin.readline

#+-() -> 괄호지우기, 값을 최소로 만들기
#-전에 괄호를 쳐야 함
stack = []
#-들어오면 괄호 치기, 다시 -들어오기 전까지 더하기
strr = input().strip()

lst = list(strr.split("-"))
total = 0
total += sum(list(map(int,lst[0].split("+")))) 
        
for temp in lst[1:]:
    plus = list(map(int,temp.split("+")))
    total -= sum(plus)
print(total)