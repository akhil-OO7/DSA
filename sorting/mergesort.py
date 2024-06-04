class Solution:
    def merge(self,arr, l, m, r): 
        # code here
        ans = [0] * (r - l + 1)
        k = 0
        left, right = l, m + 1
        
        while left <= m and right <= r:
            if arr[left] <= arr[right]:
                ans[k] = arr[left]
                k += 1
                left += 1
            else:
                 ans[k] = arr[right]
                 k += 1
                 right += 1
        
        while left <= m:
            ans[k] = arr[left]
            left += 1
            k += 1
        
        while right <= r:
            ans[k] = arr[right]
            right += 1
            k += 1
        
        for i in range(k):
            arr[l + i] = ans[i]
        
    def mergeSort(self,arr, l, r):
        #code here
        if l < r:
            mid = (l + r) // 2
            self.mergeSort(arr, l, mid)
            self.mergeSort(arr, mid + 1, r)
            self.merge(arr, l, mid, r)

# Raw code
def merge(arr, l, m, r):
    tmp = [0] * (r - l + 1)
    left, right, k = l, m + 1, 0
    
    while left <= m and right <= r: 
        if arr[left] <= arr[right]:
            tmp[k] = arr[left]
            left += 1
        else:
            tmp[k] = arr[right]
            right += 1
        k += 1
    
    while left <= m:
        tmp[k] = arr[left]
        left += 1
        k += 1
    
    while right <= r:
        tmp[k] = arr[right]
        right += 1
        k += 1
    
    for i in range(k):
        arr[l + i] = tmp[i]

def mergeSort(arr, l, r):
    if l < r:
        mid = (l + r) // 2
        mergeSort(arr, l, mid)
        mergeSort(arr, mid + 1, r)
        merge(arr, l, mid, r)
        
if __name__ == "__main__":
    arr = [5,123,3,13,5,6,4,7,9,100]
    print('array before sorting: ', arr)
    n = len(arr)
    l, r = 0, n - 1
    mergeSort(arr, l, r)
    print('array after sorting: ', arr)
