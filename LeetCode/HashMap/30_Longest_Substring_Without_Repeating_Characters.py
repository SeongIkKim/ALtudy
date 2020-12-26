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


# solution

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        max_length = start = 0  # pointer 1 : start
        for index, char in enumerate(s):  # pointer 2 : index
            # 이미 등장했던 철자라면 start 위치 갱신
            # start <= used[char]를 체크해 start 위치를 반복 철자 다음 인덱스로 당겨옴
            if char in used and start <= used[char]:
                start = used[char] + 1
                # 최대부분 문자열 길이 갱신
            else:
                max_length = max(max_length, index - start + 1)

            # 현재 문자의 위치 삽입
            used[char] = index

        return max_length

'''
44ms(98.45%)
14.4MB(39.81%)
1. 투포인터 사용이 스무스해야함..(start와 index)
2. enumerate를 사용한 간편한 index 및 철자구성
3. max함수를 이용한 max_length 갱신
'''
