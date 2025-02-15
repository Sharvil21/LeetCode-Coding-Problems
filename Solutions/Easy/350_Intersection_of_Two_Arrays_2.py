class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counts = Counter(nums1)
        output = []

        for i in nums2:
            if counts[i] > 0:
                output = output + [i]
                counts[i] = counts[i]-1
        return output
