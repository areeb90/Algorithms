# arr is the array to be searched, target is the number to be searched in the array
def binary_search(arr, target):
    # iterationCount is the number of iterations it took to find the target number
    iterationCount = 0
    min = 0                         # min is the minimum index of the array
    max = len(arr)-1                # max is the maximum index of the array
    while min <= max:               # while the minimum index is less than or equal to the maximum index
        mid = (min + max)//2        # mid is the middle index of the array
        # print(arr[mid])
        iterationCount += 1         # increment the iterationCount by 1
        if arr[mid] == target:      # if the middle index of the array is equal to the target number
            return str(target) + " found in the array after " + str(iterationCount) + " iterations."

        elif arr[mid] > target:     # if the middle index of the array is greater than the target number
            max = mid-1             # set the maximum index to the middle index minus 1

        else:                       # if the middle index of the array is less than the target number
            min = mid + 1           # set the minimum index to the middle index plus 1

    return str(target) + " not found in the array after " + str(iterationCount) + " iterations."


# Driver Code`
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
target = 7
print(binary_search(arr, target))
