class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ans = 0

        freq_chars = {}

        for char in chars:
            freq_chars[char] = freq_chars.get(char,0) + 1

        for word in words:

            freq_words = {}

            for char in word:
                freq_words[char] = freq_words.get(char,0) + 1

            can_form = True
            for char in freq_words:
                if freq_words[char] > freq_chars.get(char,0):
                    can_form = False
                    break
            if can_form:
                ans += len(word)
        return ans