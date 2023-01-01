def countingSort(arr):
    # Write your code here
    n=100
    list2=[]
    for i in range(n):
        list2.append(0)
    for i in arr:
        list2[i]=list2[i]+1
    return list2
