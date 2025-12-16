class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        lcp = ""
        smallest = len(strs[0])

        for s in strs:
            smallest = min(len(s), smallest)
        
        for i in range(smallest):
            current_char = strs[0][i]
            for s in strs:
                if s[i] != current_char:
                    return lcp
            lcp += current_char
            
        return lcp