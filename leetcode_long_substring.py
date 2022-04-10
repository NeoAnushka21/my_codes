class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # s = abcabcbb
        start_idx = 0
        end_idx = 0
        max_len_sub = 0
        my_dict = {}

        while end_idx < len(s):
            if s[end_idx] in my_dict and my_dict[s[end_idx]] >= start_idx:
                start_idx = my_dict[s[end_idx]] + 1
            max_len_sub = max(max_len_sub, end_idx - start_idx + 1)
            my_dict[s[end_idx]] = end_idx
            end_idx += 1
        return max_len_sub


obj = Solution()
obj.lengthOfLongestSubstring("abcabcbb")
