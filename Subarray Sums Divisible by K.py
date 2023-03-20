class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        cur_sum = 0
        my_dic = defaultdict(int)
        
        for i in range(len(nums)):
            cur_sum += nums[i]
            if cur_sum % k == 0:
                count += 1
            if cur_sum % k in my_dic:
                count += my_dic[cur_sum % k]

            my_dic[cur_sum % k] += 1

        return count
