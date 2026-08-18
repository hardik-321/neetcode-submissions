class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = 0
        b = 0
        idx = 0
        ans = []
        for i in nums:
            a = target - i
            if a in nums:
                idx = nums.index(a)
                if b != idx:
                    if b < idx:
                        ans.append(b)
                        ans.append(idx)
                    else:
                        ans.append(idx)
                        ans.append(b)
                    break
            
            b += 1
        return ans
