"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".


Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.


Constraints:
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters if it is non-empty.
"""

from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
    # Time O(nlogn + m), Space O(1)
    strs.sort()
    result = ""
    for i in range(min(len(strs[-1]), len(strs[0]))):
        if strs[0][i] != strs[-1][i]:
            break
        result += strs[0][i]
    return result
