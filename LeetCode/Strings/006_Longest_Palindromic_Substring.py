
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
        # 빈 문자열 케이스 처리
        if not s:
            return ""
        max_length_substring = s[0] # palindrome 없을때의 default
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

# 1st solution

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 팰린드롬 판별 및 투 포인터 확장
        def expand(left: int, right: int) -> str:
            # 1. 두 포인터가 끝에 닿을 때까지
            # 2. 기존에서 좌우 한칸씩 확장하여 회문판별 - 확장 전까지는 이미 회문임이 판별되었음
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1 : right]

        # 길이가 1 이하일때 또는 전체가 palindrome일때 빠르게 리턴
        if len(s) < 2 or s == s[::-1]:
            return s

        result = ''

        for i in range(len(s) -1):
            # 다음 요소들을 길이 기준으로 비교한다.
            # 1. 지금까지 회문 중 가장 긴 회문 - result
            # 2. 현재 포인터 i를 기준으로 두 문자, 즉 짝수 회문 - expand(i, i+1)
            # 3. 현재 포인터 i를 기준으로 세 문자, 즉 홀수 회문 - expand(i, i+2)
            # 한번 expand에 들어가면, 그 회문을 기준으로 가장 긴 회문으로 확장한다(while문)
            result = max(result, expand(i,i+1), expand(i,i+2), key=len)

'''
236ms(94.29%)
14.2MB(48.80%)
1. DP보다 빠른 투포인터 방식
2. 회문은 홀수, 짝수로 나누어 확장형식으로 검사할 수 있다는 것
'''
