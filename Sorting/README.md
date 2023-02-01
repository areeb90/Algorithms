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
![image](https://user-images.githubusercontent.com/70211234/214935489-8d952d44-912b-4cb2-a505-d7cf91f3651d.png)

Bubble sort is a simple and inefficient sorting algorithm that repeatedly steps through the list to be sorted, compares each pair of adjacent items and swaps them if they are in the wrong order. The pass through the list is repeated until no swaps are needed, which indicates that the list is sorted.


## How to implement it :

## Time Complexity:

The time complexity of the bubble sort algorithm is 
- O(n^2) in the worst and average case  
- O(n) in the best case (when the input array is already sorted). 

This is because in the worst case scenario, the algorithm needs to iterate through the entire array n times, and in each iteration, it needs to compare and swap n-1 elements.

## Space Complexity:

The space complexity of the bubble sort algorithm is 
- O(1) as it only requires a constant amount of additional memory to store temporary variables for swapping elements.

## Note:

It's important to note that bubble sort is not efficient and not the best choice for sorting large arrays and it's not recommended to use it, there are better sorting algorithms that have better time and space complexity such as Quick sort, merge sort, and heap sort.



# ALL ABOUT MERGE SORT:

![image](https://user-images.githubusercontent.com/70211234/215998364-cf9f6786-9096-4251-b90c-1afa1a3248bc.png)


Merge sort is a divide-and-conquer sorting algorithm that works by breaking down a larger array into smaller sub-arrays, sorting each sub-array, and then merging the sub-arrays back together in a sorted order. The basic idea behind merge sort is to divide the array into two equal halves, sort each half, and then merge the two sorted halves back together.

## How to implement it :

- The algorithm starts by dividing the input array into two equal halves and recursively sorting each half. 
- Once the halves are sorted, the algorithm uses a merge function to merge the two sorted halves back together. 
- The merge function compares the first element of each half and adds the smaller of the two elements to the final, sorted array. 
This process is repeated until all elements from both halves have been added to the sorted array.

## Time Complexity:

- The time complexity of merge sort is O(n log n) in the average and worst case. This is because the algorithm divides the array into two halves on each recursive call, and the number of recursive calls is logarithmic to the size of the array. 
- Additionally, the merge step of the algorithm takes O(n) time because it needs to compare and merge each element from the two sorted halves. 

## Space Complexity:

- The space complexity of merge sort is O(n) because it needs to create a new array to store the sorted elements.

## Note:

- Merge sort is a stable sort, meaning that it preserves the relative order of elements with equal keys. It is also a very efficient sorting algorithm for large data sets or data sets that are already partially sorted or reverse-sorted.
- Merge sort is also easily implemented in both serial and parallel computing environments, making it well suited for large-scale data processing and sorting tasks.
- In-memory sorting: Merge Sort is often used as the sorting algorithm in the C++ STL sort() function, Java's Arrays.sort() method, and other in-memory sorting libraries.
- External sorting: When dealing with very large data sets that do not fit in memory, Merge Sort can be used to sort the data in a distributed or external system. This is done by reading chunks of data into memory, sorting them, and then merging the sorted chunks back together.
- Distributed systems: Merge Sort can be easily parallelized, making it a good choice for sorting data in distributed systems. For example, it can be used in a MapReduce architecture to sort data on multiple machines.
- Search engines: Merge Sort is often used to sort data in search engines. The sorted data is then used to quickly perform lookups and searches.
- Version control systems: Merge Sort is used in many version control systems to merge changes from multiple branches into a single branch.


