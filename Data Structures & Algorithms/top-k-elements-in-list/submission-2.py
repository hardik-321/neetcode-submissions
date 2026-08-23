class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        ans = []

        for i in nums:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        
        top = sorted(count.items(), key=lambda x:x[1], reverse=True)[:k]

        ans = [x[0] for x in top]

        return ans
