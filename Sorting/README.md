# ALL ABOUT SELECTION SORT
![image](https://user-images.githubusercontent.com/70211234/213745916-358dcf20-8eba-40a1-a3f1-b558027a6002.png)


Selection sort is a simple sorting algorithm that repeatedly selects the smallest element from the unsorted part of the array and appends it to the sorted part of the array.

## How to implement it:

The algorithm uses two nested loops:

- The outer loop iterates through each element of the input array.
- The inner loop iterates through all elements to the right of the outer loop's current element.
- In each iteration of the inner loop, the function compares the current element to the element at the minimum index.
- If the current element is smaller than the element at the minimum index, the minimum index is updated to the current index.
- After the inner loop completes, the element at the minimum index is swapped with the current element of the outer loop.
- The outer loop continues until the entire array is sorted.

## Advantages:

- Selection sort is a simple algorithm to implement and understand, making it a good choice for educational purposes.
- Selection sort is efficient for small data sets or for sorting arrays that are already partially sorted.
- Selection sort is a good choice when memory space is a concern.

## Disadvantages:

- Selection sort is inefficient for large data sets because of its quadratic time complexity.
- Selection sort requires n-1 passes through the array, which can be time-consuming for large data sets.


## Note:
It's important to note that selection sort is not the most efficient sorting algorithm, but it can be useful for small data sets or for sorting arrays that are already partially sorted. It is also an easy algorithm to understand, which is why it's a popular topic in coding interviews.



## Time Complexity:

- Best Case: O(n^2)

- Average Case: O(n^2)

- Worst Case: O(n^2)

Selection sort has a quadratic time complexity in all cases, making it inefficient for large data sets. This is because in each iteration of the outer loop, the algorithm needs to iterate through all remaining elements in the array to find the smallest element.


## Space Complexity:

- O(1)

Selection sort has a constant space complexity, as it sorts the input array in place and does not require any additional memory. The only memory used is a temporary variable used for swapping the elements.

It's worth noting that selection sort can be useful for small data sets or for sorting arrays that are already partially sorted or when memory space is a concern.

# ALL ABOUT INSERTION SORT

![image](https://user-images.githubusercontent.com/70211234/214934253-15d91aaf-d539-4f6f-892b-bde47f4f47ff.png)

Insertion sort is a simple sorting algorithm that builds the final sorted list one item at a time. It repeatedly takes an element from the unsorted list and inserts it into the correct position in the sorted list.

## How to implement it :

Here is how the algorithm works in detail:

- Start with an empty sorted list and an unsorted list of elements.
- Take the first element from the unsorted list and insert it into the correct position in the sorted list.
- Repeat step 2 for each remaining element in the unsorted list.
- The algorithm stops when all elements have been added to the sorted list.


## Time Complexity:

- Best Case O(n)
- Avg case O(n^2)
- Worst Case O(n^2)


## Space Complexity:

- O(1) As it is inplace sorting algorithm


## Time Complexity Explaination:

Insertion sort is an in-place and stable sorting algorithm, meaning that it sorts the input array in place and preserves the relative order of equal elements. It has a time complexity of O(n^2) in the worst case, but it can be efficient for small data sets or for sorting arrays that are already partially sorted.

The best case of Insertion sort is O(n) when the input array is already sorted, it goes through the input array once and doesn't make any swap, it simply keeps moving the next element to the right, this process is known as "shifting" and has a time complexity of O(n).

The average case is also O(n^2), as it has to iterate through the array multiple times and make multiple comparisons and swaps.

## Note:
It's worth noting that Insertion sort is not the most efficient sorting algorithm, but it can be useful for small data sets or for sorting arrays that are already


# ALL ABOUT QUICK SORT:

## How to implement it :

## Time Complexity:

## Space Complexity:

## Note:


# ALL ABOUT BUBBLE SORT:

## How to implement it :

## Time Complexity:

## Space Complexity:

## Note:


# ALL ABOUT MERGE SORT:

## How to implement it :

## Time Complexity:

## Space Complexity:

## Note:



