"""
Given a string s, find the length of the longest substring without duplicate characters.

 
Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""


def lengthOfLongestSubstring(s: str) -> int:
    # Time O(n), Space O(1)
    left = curr_length = result = 0

    for right in range(len(s)):
        curr_length += 1

        while s[right] in s[left:right]:
            left += 1
            curr_length -= 1

        result = max(result, curr_length)

    return result
