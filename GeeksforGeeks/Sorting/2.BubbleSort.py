# def BubbleSort(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range(n-1-i):
#             if arr[j]>arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#
# arr = [64, 34, 25, 12, 22, 11, 90]
#
# BubbleSort(arr)
#
# print("BubbleSort: ")
# for i in range(len(arr)):
#     print ("%d" %arr[i],end=" ")


# but here TC = O(n*2) even if array is sorted

# so Optimized Implementation:

def BubbleSort(arr):
    n = len(arr)
    swapped = False

    for i in range(n):
        for j in range(n-1-i):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if swapped == False:
            break

arr = [64, 34, 25, 12, 22, 11, 90]

BubbleSort(arr)

print("BubbleSort: ")
for i in range(len(arr)):
    print ("%d" %arr[i],end=" ")
