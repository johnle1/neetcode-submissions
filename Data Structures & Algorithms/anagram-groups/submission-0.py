class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 1: uisng brute force -> O(N^2)
        # 2: using dictionary -> O(N)
        
        # Edge Case
        if len(strs) == 0 or len(strs) == 1:
            return [strs]
        dic_tracking = collections.defaultdict(list)
        for word in strs:
            count = [0] * 26 
            
            for char in word:
                count[ord(char) - ord('a')] += 1
                
            
            key = tuple(count) #  Convert the count list to a tuple (lists can't be dictionary keys, but tuples can)
            
            # 4. Append the original word to the list for this frequency key
            dic_tracking[key].append(word)
            
        # 5. Return all the grouped anagrams as a list of lists
        return list(dic_tracking.values())
