from collections import deque

def solution(s):
    stack=[]
    for i in s:
        stack.append(i)
        if len(stack)==1:
            continue
        elif stack[-1]==stack[-2]:
            stack.pop()
            stack.pop()
    if len(stack)==0:
        return 1
    else:
        return 0
