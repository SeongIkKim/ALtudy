import re

# Not Completed

class Solution:
    def myAtoi(self, s):
        s = s.strip()
        s = re.findall('^[+\-]?\d+', str)

        return


if __name__ == '__main__':
    S = Solution()
    s = "42"
    print(S.myAtoi(s))


