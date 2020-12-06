import collections
from itertools import permutations
from typing import List

# 1st try

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs = ["", ""]
        anagrams = []  # return할 set

        while strs:

            anagram_set = []  # 각 word에 대한 anagram set
            word_anagrams = tuple(permutations(list(strs[0]), len(strs[0])))  # permutation으로 anagram만들기

            for word_anagram in word_anagrams:
                str_word_anagram = ''.join(word_anagram)
                # print(f"word:{word},str_word_anagram:{str_word_anagram}")

                if str_word_anagram in strs:
                    anagram_set.append(str_word_anagram)
                    strs.remove(str_word_anagram)

            anagrams.append(anagram_set)

        return anagrams

'''
실패(1:30)
testcase
Input ["", ""]
Output [[""],[""]]
Expected [["",""]]
'''

# 1st solution

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 모든 애너그램은 sorting했을때 같은 키를 가지므로, 하나로 묶기 위해 dict 선언.
        # 없는 키에 최초삽입했을 경우 value를 빈 list로 초기화하기 위해, defaultDict를 사용한다.
        anagrams = collections.defaultdict(list)

        for word in strs:
            # 정렬하면, 키가 같은 것끼리 모을 수 있다.
            # 해당 키의 value, 즉 에너그램 리스트에 append한다
            anagrams[''.join(sorted(word))].append(word)

        # value값(에너그램 리스트)만 빼서 반환
        return anagrams.values()

'''
88ms(95.10%)
17.6MB(48.29%)

1. dict, 특히 defaultdict로 에너그램을 묶을 수 있는 것
2. 에너그램 비교는 sort로 하면 편한 것
'''

'''
python의 sort는 TimSort로 만들어져있다.
TimSort는 실제로는 대부분의 데이터들이 이미 정렬된 상태일 것이라 가정한다(따라서 이론보다 현업에서 더 유용한 알고리즘이다)
병합정렬과 삽입정렬을 휴리스틱하게 조합하여 사용하는 알고리즘으로,
최선의 경우 O(n), 최악의 경우 O(n logn)이라는 성능을 가진다.
'''
