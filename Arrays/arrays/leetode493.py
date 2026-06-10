class Solution:
    def reversePairs(self, nums):
        
        def merge_sort(arr, low, high):
            if low >= high:
                return 0
            
            mid = (low + high) // 2
            
            count = merge_sort(arr, low, mid)
            count += merge_sort(arr, mid + 1, high)
            
            # Count reverse pairs
            j = mid + 1
            for i in range(low, mid + 1):
                while j <= high and arr[i] > 2 * arr[j]:
                    j += 1
                count += (j - (mid + 1))
            
            # Merge step
            temp = []
            left, right = low, mid + 1
            
            while left <= mid and right <= high:
                if arr[left] <= arr[right]:
                    temp.append(arr[left])
                    left += 1
                else:
                    temp.append(arr[right])
                    right += 1
            
            while left <= mid:
                temp.append(arr[left])
                left += 1
            
            while right <= high:
                temp.append(arr[right])
                right += 1
            
            # Copy back
            for i in range(len(temp)):
                arr[low + i] = temp[i]
            
            return count
        
        return merge_sort(nums, 0, len(nums) - 1)