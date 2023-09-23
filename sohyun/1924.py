x, y = map(int, input().split(' '))
num = 31
month = [0,3,0,1,0,1,0,0,1,0,1,0]
day = ['MON','TUE','WED','THU','FRI','SAT','SUN']

#3월 24일이다 -> 2월까지의 수는 3이니까 31*2 - 3 + Y 니까 토요일
rest_day = 0
for i in range(x-1):
    rest_day += month[i]

total_num = num * (x-1) - rest_day + y
result = day[total_num % 7 - 1]
print(result)

