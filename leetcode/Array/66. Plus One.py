class Solution:
    def plusOne(self, digits):
        digits.insert(0, 0)
        if digits[-1] == 9:
            to_plus = True
        else:
            digits[-1] += 1
            to_plus = False

        for i in range(len(digits) - 1,  -1, -1):
            if to_plus:
                if digits[i] != 9:
                    digits[i] += 1
                    to_plus = False
                else:
                    digits[i] = 0
                    to_plus = True

        if digits[0] == 0:
            return digits[1::]
        else:
            return digits


solution = Solution()
print(solution.plusOne([8,9,9,9]))