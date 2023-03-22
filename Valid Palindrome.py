class Solution:
    def isPalindrome(self, st: str) -> bool:
        l = 0
        r = len(st)-1
        while r > l:
            if not st[r].isalnum():
                r-=1
                continue
            if not st[l].isalnum():
                l+=1
                continue
            if st[r].lower() != st[l].lower():
                return False
            r-=1
            l+=1
        print(l,r)
        return True
