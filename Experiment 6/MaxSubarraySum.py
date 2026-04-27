from collections import defaultdict

class Solution:
    def maximumSubarraySum(self, nums, k):
        freq = defaultdict(int)
        curr_sum = 0
        ans = 0
        
        left = 0
        
        for right in range(len(nums)):
            # include new element
            curr_sum += nums[right]
            freq[nums[right]] += 1
            
            # maintain window size k
            if right - left + 1 > k:
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                curr_sum -= nums[left]
                left += 1
            
            # check distinct condition
            if right - left + 1 == k and len(freq) == k:
                ans = max(ans, curr_sum)
        
        return ans
