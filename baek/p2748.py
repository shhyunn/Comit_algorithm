i = 0
fib = [0,1]
while i < 90:
    new = int(fib[i]) + int(fib[i+1])
    fib.append(new)
    i += 1
n = int(input())
print(fib[n])