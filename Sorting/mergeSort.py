def merge_sort(arr):                                   
    if len(arr) > 1:                       # if the length of the array is greater than 1
        
        mid = len(arr)//2                  # find the middle of the array
        left_arr = arr[ : mid]             # split the array into two halves
        right_arr = arr[mid : ]            # split the array into two halves

        merge_sort(left_arr)               # recursively call merge_sort on the left half
        merge_sort(right_arr)              # recursively call merge_sort on the right half


        i = 0                               # i is the index of the left half
        j = 0                               # j is the index of the right half
        k = 0                               # k is the index of the merged array



        while i < len(left_arr) and j < len(right_arr):         # while i and j are less than the length of the left and right halves
            if left_arr[i] < right_arr[j]:                      # if the left half is less than the right half
                arr[k] = left_arr[i]                            # set the value of the merged array at index k to the value of the left half at index i
                i +=1                                           # increment i

            else:                                               # if the right half is less than the left half
                arr[k] = right_arr[j]                           # set the value of the merged array at index k to the value of the right half at index j
                j +=1                                           # increment j
            k +=1                                               # increment k

        while i < len(left_arr):                                # while i is less than the length of the left half
            arr[k] = left_arr[i]                                # set the value of the merged array at index k to the value of the left half at index i

            i +=1                                               # increment i
            k+=1                                                # increment k

        while j < len(right_arr):                               # while j is less than the length of the right half
            arr[k] = right_arr[j]                               # set the value of the merged array at index k to the value of the right half at index j

            j +=1                                               # increment j
            k+=1                                                # increment k
    return arr                                                  # return the merged array


print(merge_sort([9,3,2,1,5,6,9,4,2,5,6,4,2,5,33,1,4,22]))

 
#Explaination of time complexity:
#The time complexity of merge sort is O(n log n) because the merge sort function is called recursively on the left and right halves of the array. The merge sort function is called log n times because the array is split in half log n times. The merge function is called n times because the merge function is called n times to merge the left and right halves of the array. Therefore, the time complexity of merge sort is O(n log n).

#Explaination of the space complexity:
#The space complexity of merge sort is O(n) because the merge sort function is called recursively on the left and right halves of the array. The merge sort function is called log n times because the array is split in half log n times. The merge function is called n times because the merge function is called n times to merge the left and right halves of the array. Therefore, the space complexity of merge sort is O(n).
