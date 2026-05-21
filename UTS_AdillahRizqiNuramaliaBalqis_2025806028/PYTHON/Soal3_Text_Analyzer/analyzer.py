from collections import Counter
from utils import clean_text, is_vowel, is_letter

class TextAnalyzer:
    def __init__(self, text: str):
        self.original_text = text
        self.text = clean_text(text)
        self.words = self.text.split()

    def count_lines(self):
        return len(self.original_text.splitlines())

    def count_words(self):
        return len(self.words)

    def most_common_words(self, n=5):
        counter = Counter(self.words)
        return counter.most_common(n)

    def count_vowels_consonants(self):
        vowels = 0
        consonants = 0

        for char in self.text:
            if is_letter(char):
                if is_vowel(char):
                    vowels += 1
                else:
                    consonants += 1

        return vowels, consonants

    def analyze(self):
        vowels, consonants = self.count_vowels_consonants()

        return {
            "lines": self.count_lines(),
            "words": self.count_words(),
            "top_words": self.most_common_words(),
            "vowels": vowels,
            "consonants": consonants
        }