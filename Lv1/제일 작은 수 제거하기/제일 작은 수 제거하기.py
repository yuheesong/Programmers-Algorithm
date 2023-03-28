def solution(arr):
    if len(arr)==1:
        return [-1]
    tmp=sorted(arr)
    arr.remove(tmp[0])
    return arr
