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
