class Solution:
    def length_longest_substring(self, s: str) -> int:

        start_idx = 0  # initializing staring index of substring
        end_idx = 0    # initializing ending index of substring
        max_len_sub = 0  # keeping the length of substring as 0
        my_dict = {}    #
        print(s)
        while end_idx < len(s):

            if s[end_idx] in my_dict and my_dict[s[end_idx]] >= start_idx:
                start_idx = my_dict[s[end_idx]] + 1
            max_len_sub = max(max_len_sub, end_idx - start_idx + 1)
            my_dict[s[end_idx]] = end_idx
            end_idx += 1

        print(max_len_sub)


obj = Solution()
obj.length_longest_substring("cbcba")
