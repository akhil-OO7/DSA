def insertionSort(self, alist, n):
    #code here
    for i in range(n):
        key = alist[i]
        j = i - 1
        while j >= 0 and key < alist[j]:
            alist[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        
