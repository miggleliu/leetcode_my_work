class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s) == (1 or 0):
            return s
        else:
            lst = [""] * numRows
            for i in range(len(s)):
                char = s[i]
                idx = i + 1  #index starts from 1 for the sake of clearness.
                m = 2 * numRows - 2
                rmd = idx % m 
                if rmd == 0:
                    row = 2
                else:
                    row = min(rmd, 2 * numRows - rmd)

                lst[row-1] += char

            output = ''
            for i in range(numRows):
                output += lst[i]

            return output
        
