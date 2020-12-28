# Work only in sorted array

import math

def JumpSearch(arr, n, x):
    step = math.sqrt(n)
    prev = 0

    while arr[int(min(step,n)-1)] < x:
        prev = step
        step += math.sqrt(n)
        if prev >= n:
            return -1

    while arr[int(prev)] < x:
        prev += 1
        if prev == min(step,n):
            return -1

    if arr[int(prev)] == x:
        return int(prev)

arr = [ 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610 ]
x = 55
n = len(arr)

result = JumpSearch(arr,n,x)

if result == -1:
    print("Not Found!")
else:
    print("Found at: ", result)


# TC = O(sqrt(n))
# SC = O(1)
