
#Time Complexity: O(2^n)   # The time complexity of the above code snippet is O(2^n) because the function calls itself twice for every iteration.
#Space Complexity: O(n)    # The space complexity of the above code snippet is O(n) because the function calls itself twice for every iteration.


def fibonacci(n):

    if n == 0:                                  # Base Case (when n is equal to 0)
        return 0                                # return 0
    elif n == 1:                                # Base Case (when n is equal to 1)
        return 1                                # return 1


    else:
        return fibonacci(n-1) + fibonacci(n-2)   # Recursive Case (when n is greater than 1)
