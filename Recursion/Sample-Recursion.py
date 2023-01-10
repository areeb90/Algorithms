
#Time Complexity: O(n)   # The time complexity of the above code snippet is O(n) because the function calls itself once for every iteration.
#Space Complexity: O(n)  # The space complexity of the above code snippet is O(n) because the function calls itself once for every iteration.

def Sample_Rescursion(n):
    if n <= 0:                              # Base Case (when n is less than or equal to 0)
        return n                            # return n
    else:
        print(n)    
        return Sample_Rescursion(n-1)       # Recursive Case (when n is greater than 0)


# Driver Code
n = 5
print(Sample_Rescursion(n))
