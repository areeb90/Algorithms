# Bubble Sort Algorithm

# Time Complexity: O(n^2)   # The time complexity of the above code snippet is O(n^2) because the function calls itself twice for every iteration.
# Space Complexity: O(1)    # The space complexity of the above code snippet is O(1) because the function calls itself twice for every iteration.


def bubble_sort(arr):                       # bubble_sort function takes in an array
    for num in range(len(arr)):             # for loop that iterates through the array
        for i in range(0, len(arr)-1):
            if arr[i] > arr[i+1]:           # if the current index is greater than the next index
                # swap the current index with the next index
                temp = arr[i]
                # swap the current index with the next index
                arr[i] = arr[i+1]
                # swap the current index with the next index
                arr[i+1] = temp
    return arr                              # return the sorted array


# Driver Code

lst = [2, 3, 1, 4, 0, 10, 9]
print(bubble_sort(lst))


# Here are some important points about bubble sort:

# Bubble sort compares each pair of adjacent elements in the list and swaps them if they are in the wrong order.

# The algorithm repeats this process until the list is sorted.

# The worst-case and average-case time complexity of bubble sort is O(n^2), which makes it inefficient for large lists.

# The best-case time complexity of bubble sort is O(n), which occurs when the list is already sorted.

# Bubble sort is a stable sorting algorithm, which means that it preserves the original order of equal elements.

# Bubble sort can be improved by using the "cocktail sort" variant, which sorts the list in both directions.

# Bubble sort is not commonly used in practice due to its poor performance, but it can be a useful learning tool for understanding the basics of sorting algorithms.
