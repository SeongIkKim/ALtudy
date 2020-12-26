import collections

# 1st try

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0 or len(s) == 1:
            return len(s)
        D = collections.defaultdict(lambda: [-1, -1, False])
        for i in range(len(s)):
            # print(s[i])
            if D[s[i]][2] == False:
                D[s[i]][1] = i
                if len(s[i:]) == len(set(s[i:])):
                    D[s[i]][0] = len(s) - i
                D[s[i]][2] = True
            else:
                D[s[i]] = [i - D[s[i]][1], i, True]
            # print(D[s[i]])
        print(D)

        return max(D.values())[0]

'''
테스트케이스 : 'aab' 통과 X
마지막 substring의 길이를 어떻게 넣을지 안떠오른다.
'''


