"""
Task 2: string_utils.py
Create a simple module with basic string operations.
"""

def capitalize_words(text):
    return text.title()

def reverse_string(text):
    return text[::-1]

def word_count(text):
    # Splits by whitespace and counts parts
    return len(text.split())

if __name__ == "__main__":
    test_str = "hello open world"
    print(f"capitalize_words: {capitalize_words(test_str)}")
    print(f"reverse_string: {reverse_string(test_str)}")
    print(f"word_count: {word_count(test_str)}")

"""
Example Output:
capitalize_words: Hello Open World
reverse_string: dlrow nepo olleh
word_count: 3
"""
