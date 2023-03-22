def arrayManipulation(n, queries):
    # Write your code here
    arr = [0]*(n+1)
    for start,end,num in queries:
        arr[start-1] += num
        if end < len(arr):
            arr[end]-=num
    sum_ = max_val = 0
    for num in arr:
        sum_+=num
        if sum_ > max_val:
            max_val = sum_
    return max_val
