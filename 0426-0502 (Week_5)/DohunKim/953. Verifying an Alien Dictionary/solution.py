## 953. Verifying an Alien Dictionary
## https://leetcode.com/problems/verifying-an-alien-dictionary/

# O(n^2) solution

class Solution:
    def isAlienSorted(self, words: list[str], order: str) -> bool:

        MAX_WORDS_LIST = 100
        MAX_LENGTH = 20
        ORDER_LENGTH = 26

        result = False  # default return value
        # check words are not more than 100
        if len(words) > MAX_WORDS_LIST:
            print(f"The numbrer of words in the list is greater than {MAX_WORDS_LIST}!")
            return False
        for i in range(len(words)):
            # check length of each word is not exceeded over 20
            if len(words[i]) > MAX_LENGTH:
                print(f"Trouble maker : {words[i]}")
                print(f"Max length of each word is greater than {MAX_LENGTH}!")
                return False

        # make order dictionary
        hash_ord = {}
        for i in range(26):
            hash_ord[order[i]] = i

        # words into hash map by aligns order
        align_list = []
        for i in range(len(words)):
            sum = 0
            for j in range(len(words[i])):
                sum += (hash_ord[words[i][j]] + 1) * (ORDER_LENGTH ** (MAX_LENGTH - j))
            align_list.append(sum)

        # if list is sorted, it means the words list is align alphabetically ordered!
        if align_list == sorted(align_list):
            result = True
        return result


def main():

    sample_words = ["word", "world", "row"]
    sample_order = "worldabcefghijkmnpqstuvxyz"

    solution = Solution()
    print(solution.isAlienSorted(words=sample_words, order=sample_order))



if __name__ == '__main__':
    main()