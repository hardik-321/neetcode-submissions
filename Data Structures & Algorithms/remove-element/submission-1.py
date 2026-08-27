class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        new_nums = []

        for i in range(0, len(nums)):
            if nums[i] == val:
                new_nums.append(i)
        
        new_nums.sort(reverse=True)

        for n in new_nums:
            nums.pop(n)
        
        return len(nums)
