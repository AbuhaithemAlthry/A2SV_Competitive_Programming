class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(x, y):
            return int(y + x) - int(x + y)

        strs = list(map(str, nums))
        strs.sort(key=cmp_to_key(compare))
        return str(int(''.join(strs)))