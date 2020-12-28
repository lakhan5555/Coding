def LinearSearch(arr, n, x):
    for i in range(n):
        if arr[i] == x:
            return i
    return -1

arr = [12,56,89,59,45]
n = len(arr)
x = 89

search = LinearSearch(arr, n, x)
if search == -1:
    print("not found!")
else:
    print("fount at index: ",search)

# TC = O(n)
