"""
string_utils.py
Reusable string-handling functions: useful for cleaning text
data such as names or labels in a dataset.
"""

def clean_text(text):
    """Strip whitespace and fix capitalization."""
    return text.strip().title()

def count_words(text):
    """Return the number of words in a string."""
    return len(text.split())

def is_palindrome(text):
    """Check if a string reads the same forwards and backwards."""
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]

def reverse_words(text):
    """Reverse the order of words in a sentence."""
    return " ".join(text.split()[::-1])


if __name__ == "__main__":
    sample = "  hello world  "
    print("Cleaned:", clean_text(sample))
    print("Word count:", count_words("the quick brown fox"))
    print("Is 'madam' a palindrome?", is_palindrome("madam"))
    print("Reversed:", reverse_words("Python is fun"))