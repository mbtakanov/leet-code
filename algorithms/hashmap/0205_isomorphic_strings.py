"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

Example 1:
Input: s = "egg", t = "add"
Output: true
Explanation:
The strings s and t can be made identical by:
Mapping 'e' to 'a'.
Mapping 'g' to 'd'.

Example 2:
Input: s = "foo", t = "bar"
Output: false
Explanation:
The strings s and t can not be made identical as 'o' needs to be mapped to both 'a' and 'r'.

Example 3:
Input: s = "paper", t = "title"
Output: true


Constraints:
1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.
"""


def isIsomorphic(s: str, t: str) -> bool:
    # Time: O(n), Space: O(1)
    a_to_b = {}
    b_to_a = {}
    for a, b in zip(s, t):
        if a in a_to_b:
            if a_to_b[a] != b:
                return False
        else:
            a_to_b[a] = b

        if b in b_to_a:
            if b_to_a[b] != a:
                return False
        else:
            b_to_a[b] = a
    return True
