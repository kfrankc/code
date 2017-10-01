# Given an array of strings, return all groups of strings that are anagrams.
#
# Note: All inputs will be in lower-case.

class Solution(object):
    def groupAnagrams(self, A):
        anagrams_map, result = collections.defaultdict(list), []
        for s in A:
            sorted_str = ("").join(sorted(s))
            anagrams_map[sorted_str].append(s)

        for anagram in anagrams_map.values():
            anagram.sort()
            result.append(anagram)

        return result

s = Solution()
result = s.groupAnagrams(["cat", "dog", "act", "mac"])
print result