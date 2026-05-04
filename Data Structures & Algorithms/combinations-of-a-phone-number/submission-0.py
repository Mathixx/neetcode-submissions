class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
            
        res = []
        letters = {'2':["a",'b','c'], '3': ['d', 'e', 'f'], '4': ['g', 'h','i'],
                    '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7':['p', 'q', 'r', 's'],
                   '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}

        def backtrack(s, curr_comb):
            if not s or len(s) == 0:
                res.append("".join(curr_comb).strip())
                return
            else:
                possible_letters = letters[s[0]]
                for l in possible_letters:
                    curr_comb += [l]
                    backtrack(s[1:], curr_comb)
                    curr_comb.pop()

        backtrack(digits, [])
        return res


        