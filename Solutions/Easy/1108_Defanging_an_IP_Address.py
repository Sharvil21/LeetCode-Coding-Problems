#First Solution
class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.','[.]')

#Second Solution
class Solution:
    def defangIPaddr(self, address: str) -> str:
        ans=""
        for i in address:
            if i!=".":
                ans+=i
            else:
                ans+="[.]"
        return ans
                
