class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        hash_1 = {}
        hash_2 = {}

        for letter in word1:
            hash_1[letter] = hash_1.get(letter, 0) + 1
        
        for letter in word2:
            hash_2[letter] = hash_2.get(letter, 0) + 1
        
        letters_1 = sorted(hash_1.keys())
        letters_2 = sorted(hash_2.keys())

        freq_1 = sorted(hash_1.values())
        freq_2 = sorted(hash_2.values())

        return True if letters_1 == letters_2 and freq_1 == freq_2 else False
