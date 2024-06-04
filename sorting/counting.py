def countSort(arr):
    m = max(arr)
    tmp = [0] * (m + 1)
    for i in range(len(arr)):
        tmp[arr[i]] += 1
    idx = 0
    for i in range(m + 1):
        while tmp[i] != 0:
            arr[idx] = i
            tmp[i] -= 1
            idx += 1
    
if __name__ == "__main__":
    arr = [5,123,3,13,5,6,4,7,9,100]
    print('array before sorting: ', arr)
    countSort(arr)
    print('array after sorting: ', arr)
