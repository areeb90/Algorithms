def binary_search(arr, target):
    min = 0
    max = len(arr)-1
    while min <=max :
        mid = (min + max)//2
        if arr[mid] == target:
            return arr[mid]
        
        elif arr[mid] > target :
            max = mid-1

        else:
            min = mid  + 1

    return -1