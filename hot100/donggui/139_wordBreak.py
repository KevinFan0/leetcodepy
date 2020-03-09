# 139. 单词拆分
"""
给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。

说明：

拆分时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。
示例 1：

输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
示例 2：

输入: s = "applepenapple", wordDict = ["apple", "pen"]
输出: true
解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
     注意你可以重复使用字典中的单词。
示例 3：

输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
输出: false
"""

class Solution:
    def wordBreak(self, s: str, wordDict: list) -> bool:
        dp = [False for _ in range(len(s)+1)]
        dp[0] = True
        for i in range(1, len(s)+1):
            for j  in range(0, i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[-1]

    def wordBreak2(self, s: str, wordDict: list) -> bool:
        # 递归 + 备忘录
        memo = {}
        return self.helper(0, memo, wordDict, s)

    def helper(self, start, memo, worddict, s):
        if start == len(s):
            return True
        if start in memo:
            return memo[start]
        for i in range(start+1, len(s)+1):
            if self.helper(i, memo, worddict, s) and s[start: i] in worddict:
                memo[start] = True
                return memo[start]
        memo[start] = False
        return memo[start]
        


s1 = Solution()
print(s1.wordBreak2("leetcode", ["leet","code"]))

