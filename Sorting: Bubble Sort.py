def countSwaps(a):
    # Write your code here
    n=0
    for j in range(len(a)):
        for i in range(len(a)-1):
            if a[i] > a[i+1]:
                temp = a[i+1]
                a[i+1]=a[i]
                a[i]=temp
                n=n+1
    print(f"Array is sorted in {n} swaps.")
    print("First Element:",a[0])
    print("Last Element:",a[len(a)-1])
