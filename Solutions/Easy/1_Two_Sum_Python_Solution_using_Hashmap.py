#Python Solution using Hashmap
#Create a hashmap first.
#Then iterate through the list. Create a 'difference' variable that is difference = target - value_in_list
#If difference exists in the hashmap, return that index
#Else, add that value along with the index into the hashmap
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for index, value in enumerate(nums):
            difference = target - value
            if difference in hashmap:
                return [index, hashmap[difference]]
            else:
                hashmap[value] = index

#This has O(n) time complexity because retriving data from a Hashmap is O(1)
