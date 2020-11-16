
# 1st try

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        max_length = 0
        lp = 0
        rp = 0

        p_lists = []
        for _ in range(len(s)):
            p_list = []
            for _ in range(len(s)):
                if rp < len(s) and s[lp] == s[rp]:
                    # print(f"lp:{lp},rp:{rp}")
                    if rp - lp >= max_length:
                        # print(f"이건 크네 ({lp},{rp})")
                        p_list.append((lp, rp))
                        max_length = rp - lp
                        # print("now max length=",max_length)
                rp += 1

            if p_list != []:
                p_lists.append(p_list[::-1])
            lp += 1
            rp = lp

        p_lists = p_lists[::-1]

        print(p_lists)

        for p_list in p_lists:
            for p in p_list:
                word = s[p[0]:p[1] + 1]
                if word == word[::-1]:
                    print(f"select:{p[0]},{p[1]}")
                    return word

'''
실패
TestCase : "aacabdkacaa"
Output : "aa"
Expected : "aca"
max_length는 잘못된 개념이었다는걸 깨달았다
'''

# 2st try:
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        max_length_substring = s[0]
        for left in range(len(s)):
            for right in range(left, len(s)):
                if s[left] == s[right]:
                    substring = s[left:right + 1]
                    if substring == substring[::-1] and len(substring) > len(max_length_substring):
                        max_length_substring = substring
        return max_length_substring

'''
5700ms(22.63%)
14.3MB(30.41%)
무식하게 O(n^2)으로 풀었다.
처음과 끝을 선비교하지 않았으면 시간초과였다.
'''
