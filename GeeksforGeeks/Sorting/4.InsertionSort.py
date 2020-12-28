def InsertionSort(array):
    n = len(array)
    for i in range(1, n):
        key = array[i]
        j = i-1
        while j >= 0 and array[j] > key:
            array[j+1] = array[j]
            j -= 1

        array[j+1] = key

array = [12, 11, 13, 5, 6]

InsertionSort(array)

print("InsertionSort: \n")

for i in array:
    print(i, end = " ")
