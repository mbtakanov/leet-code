"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false


Constraints:
1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
"""


def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    # For lowercase English letters both solutions have O(n) time and
    # O(1) space, but constant factors matter in real performance.
    # The array solution has better constants.

    # Lowercase English letters: Time O(n), Space O(1)
    # Unicode characters: Time O(n), Space O(n)
    # return Counter(s) == Counter(t)

    # For lowercase English letters: Time O(n), Space O(1)
    freq = [0] * 26
    for ch1, ch2 in zip(s, t):
        freq[ord(ch1) - 97] += 1
        freq[ord(ch2) - 97] -= 1
    return all(x == 0 for x in freq)
