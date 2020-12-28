# Find subarray with given sum
# handles Negative Number


def subArraySum(arr, n, sum):
    curr_sum = 0
    map = {}
    for i in range(n):
        curr_sum += arr[i]

        if curr_sum == sum:
            print("Found bw indexes 0 and ",i)
            return 1

        if (curr_sum -sum) in map:
            print("found bw ",map[curr_sum-sum]+1," and ",i)
            return 1

        map[curr_sum] = i

    print("No subarray found")

arr = [10,2,-2,-20,10]
n = len(arr)
sum = -10

subArraySum(arr, n, sum)

# TC = O(n)
# SC = O(n)          
