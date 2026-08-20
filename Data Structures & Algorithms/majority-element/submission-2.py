class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums_length = len(nums)
        count_s = {}
        for i in nums:
            if i in count_s:
                count_s[i] += 1
            else:
                count_s[i] = 1
            
        for n in count_s:
             if count_s[n] > nums_length/2:
                return n