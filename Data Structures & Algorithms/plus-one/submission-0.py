class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        string = ""
        for i in digits:
            string+=str(i)
        integer = int(string)
        res = integer+1
        
        digit_list = [int(digit) for digit in str(res)]
        return digit_list
        