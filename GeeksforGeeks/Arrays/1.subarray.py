# Given an unsorted array of nonnegative integers,
# find a continuous subarray which adds to a given number.


# def subArraySum(arr, n, sum)
#
#     for j in range(n):
#         result = arr[j]
#         z = j+1
#         while z <= n:
#             if result == sum:
#                 print("%d %d"%(j,z-1))
#                 return 1
#
#             if result > sum or z == n:
#                 break
#             result += arr[z]
#             z += 1
#     print("Not Found")
#     return 0
# arr = rr = [15, 2, 4, 8, 9, 5, 10, 23]
# n = len(arr)
# sum = 23
#
# subArraySum(arr,n,sum)



# TC = O(n*2)
# SC = O(1)


# Efficient Solution

def subArraySum(arr, n, sum):
    curr_sum = arr[0]
    start = 0

    i = 1

    while i <= n:
        while curr_sum > sum and start < (i-1) :
            curr_sum = curr_sum - arr[start]
            start += 1
        if curr_sum == sum:
            print("Found between %d and %d"%(start, i-1))
            return 1

        if i < n:
            curr_sum += arr[i]
        i += 1

    print("No subarray found")
    return 0

arr = rr = [15, 2, 4, 8, 9, 5, 10, 23]
n = len(arr)
sum = 23

subArraySum(arr,n,sum)


# TC = O(n)
# SC = O(1)
