# Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Medium
# Given a string, find the length of the longest substring without repeating characters.
# Example 1:
# Input: "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:  # if string is empty
            return 0
        if len(s) == 1:  # if string has only one character
            return 1
        max_length = 0
        for i in range(len(s)):  # iterate over all characters
            for j in range(
                i + 1, len(s) + 1
            ):  # iterate over all substrings starting at character i
                if (
                    len(set(s[i:j])) == j - i
                ):  # if current substring has no duplicate characters
                    max_length = max(max_length, j - i)  # update max length
                else:
                    break
        return max_length
