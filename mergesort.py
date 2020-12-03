'********** MERGE SORT **********'

'''
TOP DOWN APPROACH or RECURSIVE APPROACH
The bottom-up merge sort algorithm first merges pairs of adjacent arrays of 1 elements
Then merges pairs of adjacent arrays of 2 elements
And next merges pairs of adjacent arrays of 4 elements
And so on....Until the whole array is merged
'''


def sort(arr,left,right):
    if left >= right:
        return

    mid = (left + right) // 2
    sort(arr,left,mid) # sort left half of mid
    sort(arr,mid+1,right) # sort right half of mid
    # print(left,mid,right)
    merge(arr,left,mid,right)

def merge(arr,left,mid,right):

    n1 = mid - left + 1
    n2 = right - mid

    L = [0] * n1
    R = [0] * n2

    for i in range(0,n1):
        L[i] = arr[left + i]

    for j in range(0,n2):
        R[j] = arr[mid + 1 + j]



    # Merge the temp arrays back into arr[l..r]
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = left     # Initial index of merged subarray

    while i < n1 and j < n2 :
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1



# Driver code to test above
arr = [12, 11, 13, 5, 6, 7,30,-1,22]
n = len(arr)
sort(arr,0,n-1)
print ("\n\nSorted array is")
print(arr)





'''
BOTTOM UP APPROACH or ITERATIVE APPROACH
The bottom-up merge sort algorithm first merges pairs of adjacent arrays of 1 elements
Then merges pairs of adjacent arrays of 2 elements
And next merges pairs of adjacent arrays of 4 elements
And so on....Until the whole array is merged


arr = []
for width in range(0,len(arr-1),2*width):

    for i in range(0,len(arr-1))
'''
