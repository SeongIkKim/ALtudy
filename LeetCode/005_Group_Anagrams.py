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
