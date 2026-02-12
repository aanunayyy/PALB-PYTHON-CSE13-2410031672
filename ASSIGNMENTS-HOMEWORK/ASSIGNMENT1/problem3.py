class Solution:
    def kthSmallest(self, arr, k):
        def quickselect(left, right):
            pivot = arr[right]
            p = left
            
            for i in range(left, right):
                if arr[i] <= pivot:
                    arr[i], arr[p] = arr[p], arr[i]
                    p += 1
            
            arr[p], arr[right] = arr[right], arr[p]
            
            if p == k - 1:
                return arr[p]
            elif p > k - 1:
                return quickselect(left, p - 1)
            else:
                return quickselect(p + 1, right)
        
        return quickselect(0, len(arr) - 1)
