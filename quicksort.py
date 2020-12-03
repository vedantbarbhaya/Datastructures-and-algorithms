'''

QUICKSORT:

Avg time complexity - O(nlogn)
worst space complexity - O(logn)

What we basically try to do with quicksort is that we select a pivot element
randomly from the array and then partition the array in such a way that all the
elements on the left side of the pivot are less than the pivot and all the
elements on the right side of the pivot are more than the pivot.

So we basically find an index for the pivot at which when the pivot is placed,
it partitions the array in a way that it matches the above condition. We do that
using the partition function which swaps the elements in a way and returns an
index which is the partitioning index.

Why Quick Sort is preferred over MergeSort for sorting Arrays?
Quick Sort in its general form is an in-place sort (i.e. it doesn’t require any
extra storage) whereas merge sort requires O(N) extra storage, N denoting the
array size which may be quite expensive. Allocating and de-allocating the extra
space used for merge sort increases the running time of the algorithm. Comparing
average complexity we find that both type of sorts have O(NlogN) average complexity
but the constants differ. For arrays, merge sort loses due to the use of extra
O(N) storage space.

read this entire article for proper info: https://www.geeksforgeeks.org/quick-sort/
'''


arr = [15,3,2,1,9,5,7,8,6]

def quicksort(arr,start,end):

    if(start >= end):
        return

    pivot = arr[(start + end) //2 ]

    # pivot = arr[start]
    part_index = partition(arr,start,end,pivot)
    quicksort(arr,start, part_index - 1)
    quicksort(arr, part_index, end)

    return arr


def partition(arr , left , right , pivot):

    while(left <= right):

        while(arr[left] < pivot and left <=len(arr)):
            left = left + 1

        while(arr[right] > pivot and right >=0):
            right = right - 1

        if(left <= right):
            arr[left], arr[right] = arr[right], arr[left]
            left = left + 1
            right= right - 1

    return left

a = quicksort(arr,0,len(arr)-1)
print(a)
