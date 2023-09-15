class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       hashmap = {}
       for i in range(0, len(nums)):
         hashmap[nums[i]]= i
       for i in range(0, len(nums)):
         complement = target - nums[i]
         if complement in hashmap and hashmap[complement] != i:
           return [i, hashmap[complement]] 
         
