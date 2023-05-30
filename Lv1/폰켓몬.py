def solution(nums):
    d={}
    for i in nums:
        d[hash(i)]=i
    if len(d)<=len(nums)//2:
        return len(d)
    else:
        return len(nums)//2
