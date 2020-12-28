# works on sorted array
# Exponential search involves two steps:

# Find range where element is present
# Do Binary Search in above found range.

def BinarySearch(arr, l, r, x):
    if l <= r:
        mid = int(l + (r-l)/2)

        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return BinarySearch(arr,l,mid-1,x)
        else:
            return BinarySearch(arr, mid+1, r,x)

    return -1

def ExponentialSearch(arr,n,x):
    if arr[0] == x:
        return 0

    i = 1

    while i < n and arr[i] <= x:
        i = i*2

    return BinarySearch(arr,i/2,min(i,n-1),x)

arr = [2,3,4,10,40]
n = len(arr)
x = 10

result = ExponentialSearch(arr,n,x)

if result == -1:
    print("Not Found!")
else:
    print("Found at index: ",result)



# TC = O(logn)

# SC = O(logn) because Recursive Binary search
# if IterativeBinarySearch then SC = O(1)
