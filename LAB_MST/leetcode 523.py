class Solution(object):
    def checkSubarraySum(self, nums, k):
        rem_index={0:-1}
        prefix_sum=0
        for i in range(len(nums)):
            prefix_sum+=nums[i]
            rem=prefix_sum%k
            if rem in rem_index:
                if i-rem_index[rem]>=2:
                    return True
            else:
                rem_index[rem]=i
        return False
