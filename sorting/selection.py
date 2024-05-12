def selectionSort(self, arr,n):
    for i in range(n - 1):
        minIdx = i
        for j in range(i, n):
            if arr[minIdx] > arr[j]:
                minIdx = j
        arr[i], arr[minIdx] = arr[minIdx], arr[i]
