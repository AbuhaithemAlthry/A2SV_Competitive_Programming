class Solution:
    # method 1 -using hashmap and prefixsum
    # def numberOfSubarrays(self, nums, k: int) -> int:
    #     prefix_sum = [0]
    #     for num in nums:
    #         if num % 2:
    #             prefix_sum.append(prefix_sum[-1] + 1)
    #         else:
    #             prefix_sum.append(prefix_sum[-1])
    #     history = defaultdict(int)
    #     res = 0
    #     for num in prefix_sum:
    #         if num - k in history:
    #             res += history[num - k]
    #         history[num] += 1
            
    #     return res
    
    # method 2 -using two sliding windows
    def numberOfSubarrays(self, nums, k: int) -> int:

        def at_most(k):
            odd = 0
            l,r,n = 0,0,len(nums)
            res = 0
            while r<n:
                if nums[r]%2:
                    odd+=1
                while odd > k:
                    if nums[l]%2:
                        odd -= 1
                    l+=1
                res += r-l+1
                r+=1
            return res
            
        return at_most(k)-at_most(k-1)
