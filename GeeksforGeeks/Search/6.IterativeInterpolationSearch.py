def IterativeInterpolationSearch(arr, l, r, x):
    while l <= r and arr[l] <= x and arr[r] >= x:
        if l==r:
            if arr[l] == x:
                return l
            return -1

        pos  = l + int((((r - l) /
            ( arr[r] - arr[l])) * ( x - arr[l])))

        if arr[pos] == x:
            return pos
        if arr[pos] > x:
            r = pos - 1
        else:
            l = pos + 1

    return -1

arr = [10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47]
n = len(arr)
x = 18

result = IterativeInterpolationSearch(arr,0,n-1,x)

if result == -1:
    print("Not Found!")
else:
    print("Found at Index: ",result)
