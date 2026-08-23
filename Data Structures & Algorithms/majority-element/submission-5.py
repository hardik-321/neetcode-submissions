class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        nums_length = len(nums)
        for i in nums:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1

            for n in count:
                if count[n] > nums_length/2:
                    return n