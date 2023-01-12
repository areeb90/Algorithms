def Quick_sort(arr):
    if len(arr) > 1:                                # if the length of the array is greater than 1

        pivot = arr[0]                              # set the pivot to the first element of the array
        left_arr = []                               # create an empty array for the left half
        right_arr = []                              # create an empty array for the right half

        for i in range(1, len(arr)):                # for i in the range of 1 to the length of the array

            if arr[i] < pivot:                      # if the value of the array at index i is less than the pivot
                left_arr.append(arr[i])             # append the value of the array at index i to the left half

            else:                                   # if the value of the array at index i is greater than the pivot
                right_arr.append(arr[i])            # append the value of the array at index i to the right half

        return Quick_sort(left_arr) + [pivot] + Quick_sort(right_arr)       # return the left half, pivot, and right half
    else:
        return arr


# driver code
arr = [9, 3, 2, 1, 5, 6, 9, 4, 2, 5, 6, 4, 22]
print(Quick_sort(arr))


#Time Complexity Explaination
#The time complexity of quick sort is O(n log n) because the quick sort function is called recursively on the left and right halves of the array. The quick sort function is called log n times because the array is split in half log n times. The for loop is called n times because the for loop is called n times to split the array into the left and right halves. Therefore, the time complexity of quick sort is O(n log n).

#Space Complexity Explaination
#The space complexity of quick sort is O(n) because the quick sort function is called recursively on the left and right halves of the array. The quick sort function is called log n times because the array is split in half log n times. The for loop is called n times because the for loop is called n times to split the array into the left and right halves. Therefore, the space complexity of quick sort is O(n).
