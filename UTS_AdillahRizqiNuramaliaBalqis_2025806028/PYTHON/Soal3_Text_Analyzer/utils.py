import string

VOWELS = "aiueoAIUEO"

def clean_text(text: str) -> str:
    """Hapus tanda baca dan ubah ke lowercase"""
    text = text.translate(str.maketrans("", "", string.punctuation))
    return text.lower()

def is_vowel(char: str) -> bool:
    return char in VOWELS

def is_letter(char: str) -> bool:
    return char.isalpha()