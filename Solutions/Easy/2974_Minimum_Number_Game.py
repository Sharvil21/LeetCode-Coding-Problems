#First solution
class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        first_min = 0
        second_min = 0
        output = []
        while len(nums) != 0:
            for i in range(len(nums)):
                first_min = min(nums)
                nums.pop(nums.index(min(nums)))
                break

            for j in range(len(nums)):
                second_min = min(nums)
                nums.pop(nums.index(min(nums)))
                break
                
            output.append(second_min)
            output.append(first_min)
            
        
        return output

#Second Solution
class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        ans = nums.copy()
        for i in range(0,len(nums),2):
            ans[i]=nums[i+1]
            ans[i+1] = nums[i]
        return(ans)                    
