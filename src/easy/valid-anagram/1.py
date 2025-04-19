class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashtable_1 = {}
        hashtable_2 = {}
        for i in s:
            if i not in hashtable_1:
                hashtable_1[i] = 1
            else:
                hashtable_1[i] += 1
        for i in t:
            if i not in hashtable_2:
                hashtable_2[i] = 1
            else:
                hashtable_2[i] += 1

        return hashtable_1 == hashtable_2

