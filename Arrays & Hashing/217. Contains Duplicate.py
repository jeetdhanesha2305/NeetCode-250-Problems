class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # using hash set
        # time complexity = O(n)
        # space complexity = O(n)
        uniq_elems = set()

        for elem in nums:
            if elem in uniq_elems:
                return True 
            else:
                uniq_elems.add(elem) 
        return False 

        # using sorting 
        # time complexity = O(n logn) 
        # space complexity = O(1)

        nums.sort()
        N = len(nums)
        i = 1 

        for i in range(1, N):
            if nums[i] == nums[i-1]:
                return True

        return False
        