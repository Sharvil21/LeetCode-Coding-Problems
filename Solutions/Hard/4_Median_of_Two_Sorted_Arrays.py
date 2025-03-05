#Usual Python Solution
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total_size = len(nums1) + len(nums2)
        final_array = sorted(nums1 + nums2)
        if total_size % 2 != 0:  # Odd case
            median_value = final_array[total_size // 2]
        else:  # Even case
            median_value = (final_array[total_size // 2 - 1] + final_array[total_size // 2]) / 2
        return median_value

