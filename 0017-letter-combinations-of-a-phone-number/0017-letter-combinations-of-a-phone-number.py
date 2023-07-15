class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        dictionary = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        dp = [""]
        for digit in digits:
            current_combinations = []
            for existing_comb in dp:
                for new_char in dictionary[digit]:
                    current_combinations.append(existing_comb + new_char)
            dp = current_combinations
        return dp