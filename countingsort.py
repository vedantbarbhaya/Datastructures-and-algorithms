# Counting sort in Python programming
# video for explaination- https://www.youtube.com/watch?v=7zuGmKfUt7s

def countingSort(array):
    size = len(array)
    output = [0] * size

    # Initialize count array
    max_val = array[0]
    for i in range(1,len(array)):
        if array[i] > max_val:
            max_val = array[i]

    count = [0] * (max_val + 1)


    # Store the count of each elements in count array
    for i in range(0, size):
        count[array[i]] += 1

    # Store the cummulative count
    for i in range(1, len(count)):
        count[i] += count[i - 1])

    # Find the index of each element of the original array in count array
    # place the elements in output array
    i = size - 1
    while i >= 0:
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1
        i -= 1

    # Copy the sorted elements into original array
    for i in range(0, size):
        array[i] = output[i]


data = [4, 2, 2, 8, 3, 3, 1]
countingSort(data)
print("Sorted Array in Ascending Order: ")
print(data)
