class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        
        def prime_factorize(n: int) -> List[Tuple[int, int]]:
            result = []

            def extract(p: int) -> None:
                nonlocal n
                if n % p == 0:
                    result.append((p, 0))
                    while n % p == 0:
                        n //= p
                        result[-1] = (p, result[-1][1] + 1)

            for p in range(2, int(n**0.5) + 1):
                extract(p)

            if n > 1:
                result.append((n, 1))

            return result
    
        s = set()
        for x in nums:
            for p, _ in prime_factorize(x):
                s.add(p)
        return len(s)