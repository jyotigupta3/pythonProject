"""
Input: s = "barfoothefoobarman", words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.
"""
import collections
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n = len(s)
        k = len(words)
        wordLength = len(words[0])
        substringSize = wordLength * k
        word_count = collections.Counter(words)
        answer = []

        def sliding_window(left):
            words_found = collections.defaultdict(int)
            words_used = 0
            excess_word = False

            # Do the same iteration pattern as the previous approach - iterate
            # word_length at a time, and at each iteration we focus on one word
            for right in range(left, n, wordLength):
                if right + wordLength > n:
                    break
                sub = s[right: right + wordLength]

                if sub not in word_count:
                    # Mismatched word - reset the window
                    words_found = collections.defaultdict(int)
                    words_used = 0
                    excess_words = False
                    left = right + wordLength

                else:
                    # If we reached max window size or have an excess word
                    while right - left == substringSize or excess_word:
                        # Move the left bound over continously
                        leftmost_word = s[left: left + wordLength]
                        left += wordLength
                        words_found[leftmost_word] -= 1
                        if words_found[leftmost_word] == word_count[leftmost_word]:
                            # This word was the excess word
                            excess_word = False
                        else:
                            # Otherwise we actually needed it
                            words_used -= 1
                    # Keep track of how many times this word occurs in the window
                    words_found[sub] += 1
                    if words_found[sub] <= word_count[sub]:
                        words_used += 1
                    else:
                        # Found too many instances already
                        excess_word = True

                    if words_used == k and not excess_word:
                        # Found a valid substring
                        answer.append(left)

        start_index = []
        for word in words:
            index = s.find(word)
            start_index.append(index)

        start_index = sorted(start_index)
        for i in range(len(start_index)):
            for j in range(i+1, len(start_index)):
                diff = abs(start_index[i] - start_index[j])
                if diff > wordLength:
                    index = start_index[i]
        left = index
        for i in range(wordLength):
            sliding_window(left+i)
        return answer

if __name__ == "__main__":
    # s = "abcbaabcabcaccbcccbbaaabaaaaaabaabcacbacaaacabcabaccbccbaaaabbbbabcaaaaabbcbcbabccbccbbcbbacbccbabcacabbcbacaabbcabcbcaacbaaaccbbcababccaabcbab"
    # words = ["cac", "bcc", "bab", "abb", "bac"]
    s = "lingmindraboofooowingdingbarrwingmonkeypoundcake"
    words = ["fooo","barr","wing","ding","wing"]
    find_string = Solution().findSubstring(s, words)
    print(find_string)