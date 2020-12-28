def IterativeBinarySearch(arr, l, r, x):
    while l <= r:
        mid = (l + r -1)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            r = mid -1
        else:
            l = mid + 1
    return - 1

arr = [ 2, 3, 4, 10, 40 ]
x = 10

result = IterativeBinarySearch(arr, 0, len(arr)-1, x)

if result == -1:
    print("Not Found")
else:
    print("Found at Index: ", result)


# TC = O(logn)
# SC = O(1)
