"""
Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".
"""

def findLongestSubstring(in_str: str, n: int) -> str:
    start = 0
    end = 0
    hash_map = {}
    # old_max= ''
    # current_max = ''
    substrings = []
    idx = 0
    while(end<len(in_str)):
        letter = in_str[end]
        if letter not in hash_map:
            hash_map[letter] = 1
        else:
            hash_map[letter] += 1
        end += 1 

        # print(hash_map, len(hash_map))
        if len(hash_map) > n:
            # print(start, end-1)
            # print(in_str[start:end-1])

            substrings.append(in_str[start:end-1])
            start = start+1
            end = start
            hash_map ={}
            # print(start, end)

        idx += 1
    print(substrings)
    return max(substrings,key= lambda x:len(x))


print(findLongestSubstring('abcba',2))

