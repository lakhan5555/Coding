def RecursiveLinearSearch(arr, l, r, x):
    if l > r:
        return -1
    if arr[l] == x:
        return l
    if arr[r] == x:
        return r
    return RecursiveLinearSearch(arr,l+1, r-1, x)

arr = [12,34,54,2,3]
n = len(arr)
x = 3
result = RecursiveLinearSearch(arr, 0, n-1, x)

if result == -1:
    print("Not Found!")
else:
    print("Found at index: ", result)                  
