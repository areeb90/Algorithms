def selection_Sort(arr):                                
    result = []                     
    for i in range(len(arr)):
        min_index = i
        for j in range(i, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        result.append(arr[min_index])
        arr[min_index], arr[i] = arr[i], arr[min_index]
    return result


a = [2, 1, 3, 4, 5, 6, 7, 1, 0, -1]
print(selection_Sort(a))


#The above code is an implementation of the selection sort algorithm. The selection sort algorithm is a simple sorting algorithm that repeatedly selects the smallest element from the unsorted part of the array and appends it to the sorted part of the array.The function takes in an input array as an argument and creates an empty list called "result". It then uses two nested for loops. 

# The outer loop iterates through each element of the input array, and the inner loop iterates through all elements to the right of the outer loop's current element.

#In each iteration of the inner loop, the function compares the current element to the element at the minimum index. If the current element is smaller than the element at the minimum index, the minimum index is updated to the current index. After the inner loop completes, the element at the minimum index is appended to the "result" list, and it's swapped with the current element of the outer loop.

# After the outer loop completes, the function returns the "result" list which contains the elements of the input array sorted in ascending order.

# It should be noted that the selection sort algorithm has a time complexity of O(n^2) which makes it inefficient for large data sets.