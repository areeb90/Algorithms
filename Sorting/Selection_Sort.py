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
