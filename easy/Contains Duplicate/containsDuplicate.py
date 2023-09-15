class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash = set()
        for i in range(0, len(nums)):
            if nums[i] in hash:
                return True
            hash.add(nums[i])
        return False