class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums_length = len(nums)
        pre_ans = ""
        ans = ""
        count_s = {}
        for i in nums:
            if i in count_s:
                count_s[i] += 1
            else:
                count_s[i] = 1
            
        for n in count_s:
            pre_ans = count_s[n]
            if pre_ans > nums_length/2:
               ans = next((k for k, v in count_s.items() if v == pre_ans), None)
               return ans 