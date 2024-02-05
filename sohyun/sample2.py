# def solution(s):
#     answer = -1
#     l = len(s) #6
#     i = 0
#     while i < len(s)-1: #i가 5보다 작을 때까지, 1
#         a1 = s[i] #a, i가 1
#         a2 = s[i+1] #a
#         if a1 == a2 and i != l-1: #1이 4가 아니라면
#             s = s[0:i]  + s[i+2:l]
#             i = 0
#         else:
#             i += 1
    
#     if len(s) >= 1:
#         answer = 0
#     else:
#         answer = 1
    
#     return answer

# print(solution("cdcd"))

def solution(s):
    answer = -1
    stt = []
    for ch in s:
        if stt and stt[-1] == ch:
            stt.pop()
        else:
            stt.append(ch)
    
    if stt:
        answer = 0
    else:
        answer = 1
    
    return answer

print(solution("baabaa"))
