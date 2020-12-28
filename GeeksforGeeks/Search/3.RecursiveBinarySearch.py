# Binary Search is for sorted array only

def RecursiveBinarySearch(arr, l, r, x):
    if l <= r:
        mid = (l + r - 1)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return RecursiveBinarySearch(arr, l, mid-1,x)
        else:
            return RecursiveBinarySearch(arr, mid+1, r, x)
    else:
        return -1

arr = [ 2, 3, 4, 10, 40 ]
x = 10

result = RecursiveBinarySearch(arr, 0, len(arr)-1, x)

if result == -1:
    print("Not Found")
else:
    print("Found at Index: ", result)


# TC = O(logn)
# SC = O(logn) because O(Logn) recursion call stack space.
