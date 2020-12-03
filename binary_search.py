'''
iterative approach
'''

def binary_search_it(arr, low, high, x):

    while(high >= low):

        mid = (high + low) // 2
        
        if arr[mid] == x:
            return mid

        elif arr[mid] > x:
            high = mid - 1

        else:
            low = mid + 1

    else:
        return -1

'''
recursive approach
'''
def binary_search_re(arr, low, high, x):

    # Check base case
    if high >= low:

        mid = (high + low) // 2

        # If element is present at the middle itself
        if arr[mid] == x:
            return mid

        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binary_search_re(arr, low, mid - 1, x)

        # Else the element can only be present in right subarray
        else:
            return binary_search_re(arr, mid + 1, high, x)

    else:
        # Element is not present in the array
        return -1

# Test array
arr = [ 2, 3, 4, 10, 40 ]
x = 10

# Function call
result1 = binary_search_re(arr, 0, len(arr)-1, x)
result2 = binary_search_it(arr, 0, len(arr)-1, x)
print(result1,result2)
