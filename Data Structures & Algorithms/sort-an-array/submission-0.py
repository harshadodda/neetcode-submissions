class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # merge sort

        def merge(arr, left, mid, right):
            leftArr = arr[left:mid + 1] # gets array from left pointer to mid pointer
            rightArr = arr[mid + 1:right + 1] # includes last value with right + 1
            i, j, k = left, 0, 0
            while j < len(leftArr) and k < len(rightArr):
                if leftArr[j] <= rightArr[k]:
                    arr[i] = leftArr[j]
                    j += 1
                else:
                    arr[i] = rightArr[k]
                    k += 1
                i += 1
            while j < len(leftArr):
                nums[i] = leftArr[j]
                j += 1
                i += 1
            while k < len(rightArr):
                nums[i] = rightArr[k]
                k += 1
                i += 1

        def mergeSort(arr, left, right):
            # split the arrays
            if left == right:
                return arr
            mid = (left + right) // 2
            mergeSort(arr, left, mid)
            mergeSort(arr, mid + 1, right)

            # merge each piece of the array
            merge(arr, left, mid, right)
            return arr

        return mergeSort(nums, 0, len(nums) - 1)

