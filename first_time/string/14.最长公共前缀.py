#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs):
        if strs == [] or strs==[""]:
            return ''
        len_ , count = len(strs[0]), len(strs)
        str_0 = strs[0]
        same_str = ''
        for i in range(len_):
            temp_r = str_0[i]
            r = [strs[j][i] if len(strs[j]) >i else 0 for j in range(1, count)]
            same = all(temp_temp_r == temp_r for temp_temp_r in r)
            if same:
                same_str += temp_r
            else:
                return same_str
        return same_str

class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        i = 0
        len_ = min([len(s) for s in strs])
        if len_ == 0:
            return ""

        for i in range(len_):
            temp = set([s[i] for s in strs])
            if len(temp) != 1:
                return strs[0][:i]
        return strs[0][:i+1]
# @lc code=end

solution = Solution()
print(solution.longestCommonPrefix(["flower","flow","flight"]))

