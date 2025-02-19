#First solution. TIme complexity is bad here. Time limit exceeded but the solution does work.
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j] and abs(i-j) <= k:
                    return True
        
        return False

#2nd solution using Dictionary and enumerate:
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
       empty_dict = {}

       for index, value in enumerate(nums):
        if value in empty_dict and index - empty_dict[value] <=k:
            return True
        else:
            empty_dict[value] = index
        
       return False
