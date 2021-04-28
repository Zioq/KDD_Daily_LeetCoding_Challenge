# 953. Verifying an Alien Dictionary
# https://leetcode.com/problems/verifying-an-alien-dictionary/

''' 

In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.


Ex1)
Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.

Ex2)
Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
'''


class Solution:
    def isAlienSorted(self, words, order):
        ''' 
        words: List[str]
        order: str
        '''

        # Create a dictionary to save a key-value related to order
        dic = {}
        # Fill up dic key: order's char - value:index number
        for s in order:
            dic[s] = order.index(s)
        
        # Create a new list to save decoded words as numbers
        new_list =[]

        for w in words:
            # Create a list to save a decoded words
            word_list = []
            for c in w:
                # Add a decoded word to the list
                word_list.append(dic[c])
            new_list.append(word_list)
        
        # new_list = [[0, 6, 1, 1, 14], [1, 6, 6, 19, 4, 14, 5, 6]]
        # zip will zip 2 element one by one
        # zip(new_list, new_list[1:]) here will combine first element(words[0]) in words with words[1]
        for w1, w2 in zip(new_list, new_list[1:]):  
            # print(w1) #[0, 6, 1, 1, 14]
            # print(w2) #[1, 6, 6, 19, 4, 14, 5, 6]
            if w1 > w2:
                return False
        return True