from collections import deque

def solution(s):
    if s[0]==")" or s[-1]=="(":
        return False
    queue=deque()
    for i in s:
        if i=="(":
            queue.append("(")
            continue
        elif i==")":
            if len(queue)==0:
                return False
            queue.popleft()
            continue
    if len(queue)==0:
        return True
    return False
