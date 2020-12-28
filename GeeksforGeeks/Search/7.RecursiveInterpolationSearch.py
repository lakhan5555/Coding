def RecursiveInterpolationSearch(arr, l, r, x):
    if l<=r and arr[l]<=x and arr[r]>=x:
        pos = l + ((r - l) // (arr[r] - arr[l]) * (x - arr[l]))

        if arr[pos] == x:
            return pos

        if arr[pos] > x:
            return RecursiveInterpolationSearch(arr,l,pos-1,x)
        else:
            return RecursiveInterpolationSearch(arr, pos+1,r,x)

    return -1

arr = [10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47]
n = len(arr)
x = 18

result = RecursiveInterpolationSearch(arr, 0, n-1, x)

if result == -1:
    print("Not Found!")
else:
    print("Found at index: ",result)                                   
