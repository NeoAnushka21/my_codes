class Solution:

    def two_sum(self, nums: [int], target: int) -> [int]:

        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    print(([i, j]))


obj = Solution()
obj.two_sum([2, 7, 11, 15], 17)
