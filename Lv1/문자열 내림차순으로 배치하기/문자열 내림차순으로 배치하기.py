def solution(s):
    up=''
    down=''
    for i in s:
        if i.isupper():
            up+=i
        else:
            down+=i
    return "".join(sorted(down,reverse=True)+sorted(up,reverse=True))
