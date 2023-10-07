class Solution:
    def knightDialer(self, n):
        if n == 1:
            return 10
        cache = {}

        neighbors = {
            0: [4, 6],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [0, 3, 9],
            5: [],
            6: [0, 1, 7],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4]
        }
        def helper(position, num_hops):
            if (position, num_hops) in cache:
                return cache[ (position, num_hops) ]

            if num_hops == 0:
                return 1

            num_sequences = 0
            for neighbor in neighbors[position]:
                num_sequences += helper(neighbor, num_hops - 1)
            cache[(position, num_hops)] = num_sequences
            return num_sequences
        

        res = 0
        for i in range(10):
            res += helper(i, n-1)
        return res % (10**9 + 7)
