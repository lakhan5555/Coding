# TC of Linear search is O(n)
# Now for worst case-
# for last element write in O(1)
# for not found write in O(n/2)

def LinearSearch(arr, n, x):
    left = 0
    right = n-1
    position = -1

    while left <= right:
        if arr[left] == x:
            position = left
            print("found at index: ", position)
            break
        if arr[right] == x:
            position = right
            print("found at index: ", position)
            break
        left += 1
        right -= 1
    if position == -1:
        print("Not Found!")

arr = [12,56,89,59,45]
n = len(arr)
x = 89

LinearSearch(arr, n, x)
