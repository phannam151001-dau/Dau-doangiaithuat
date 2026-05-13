class Solution:
    def containsNearbyDuplicate(self, nums, k):
        vi_tri = {}

        for i in range(len(nums)):
            if nums[i] in vi_tri:
                if i - vi_tri[nums[i]] <= k:
                    return True

            vi_tri[nums[i]] = i

        return False