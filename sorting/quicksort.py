def quickSort(arr, l, r):
    if l < r:
        pivot = partition1(arr, l, r)
        # pivot = partition2(arr, l, r)
        quickSort(arr, l, pivot - 1)
        quickSort(arr, pivot + 1, r)
    
def partition(arr, low, high):
    pivot = arr[high]
    i = low
    j = high - 1
    while i < j:
        while i < high and arr[i] <= pivot:
            i += 1
        while j > low and arr[j] > pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j] , arr[i]
    if arr[i] > pivot:
        arr[i], arr[high] = arr[high], arr[i]
    return i

# 2nd way to write partition
def partition2(arr, low, high):
    pivot = arr[high]
    i = low
    for j in range(low, high):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    if arr[i] > pivot:
        arr[i], arr[high] = arr[high], arr[i]    
    return i
            
    
if __name__ == "__main__":
    arr = [5,123,3,13,5,6,4,7,9,100]
    print('array before sorting: ', arr)
    n = len(arr)
    l, r = 0, n - 1
    quickSort(arr, l, r)
    print('array after sorting: ', arr)
