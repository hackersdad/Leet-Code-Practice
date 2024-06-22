# def twoSum(self, nums: List[int], target: int) -> List[int]:
        
    #     for i in range(len(nums)):    
    #         if target - nums[i] in nums[i+1:]:
    #             for j in range(i+1,len(nums)):
    #                 if target - nums[i] == nums[j]:
    #                     return [i,j]

def twoSum(self, nums: List[int], target: int) -> List[int]:
    
    seen = {}
    for i, n in enumerate(nums):    
        c = target - nums[i]
        if c in seen:
            return [seen[c],i]
        seen[n] = i