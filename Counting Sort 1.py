def countingSort(arr):
    # Write your code here
    dict=[0]*100
    for ele in arr:
        if dict[ele]:
            dict[ele]=dict[ele]+1
        else:
            dict[ele]=1
    return dict
