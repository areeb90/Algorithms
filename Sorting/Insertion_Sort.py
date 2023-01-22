def selection_Sort(arr):                                # defining the function
    res = []                                            # empty array initialization
    for i in range(len(arr)):                           # iterate over the array
        min_index = i                                   # set the first element to the minimum element
    
        for j in range(i, len(arr)):                    # This nested loop iterates over the remaining elements in the array starting from the current index i.
            if arr[j] < arr[min_index]:                 # This line compares the current element with the minimum element.
                min_index = j                           # This line updates the minimum index to the current index j if the current element is smaller than the minimum element.
        res.append(arr[min_index])                          # Add minimum element tp the sorted list
        arr[min_index], arr[i] = arr[i], arr[min_index]     # swaps the minimum element with the currrent element

    return res                                              # return the resulting list


print(selection_Sort([1,9,0,9,0]))                # Driver code
