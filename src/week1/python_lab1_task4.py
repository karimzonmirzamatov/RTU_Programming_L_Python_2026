"""
Task 4 – Text-based Arithmetic Analyzer
---------------------------------------
Create a text-based analyzer made of small helper functions.

Rules used by all functions:
- Words are pieces of text separated by whitespace (use .split()).
- A NUMBER is a word that is a whole integer, optionally with a leading
  minus sign, e.g. "7", "42", "-3".
  Punctuation at the end of a word is ignored, so "5," "10." "8!" count
  as 5, 10 and 8. Use word.rstrip(".,!?;:") to remove it.
  Decimals ("3.5") and mixed words ("abc123") are NOT numbers.
- You do not need the `re` module; .split(), .rstrip() and .isdigit()
  are enough.

Helper functions:
- count_characters(text) -> int    : characters that are not whitespace
- count_words(text)      -> int    : number of words
- extract_numbers(text)  -> list   : list of ints, in the order they appear
- analyze_text(text)     -> dict   : combines the helpers (see below)

analyze_text() returns a dict with exactly these keys:
    "characters" : int   (from count_characters)
    "words"      : int   (from count_words)
    "numbers"    : list  (from extract_numbers)
    "sum"        : int   (sum of the numbers, 0 if there are none)
    "average"    : float (average of the numbers, 0.0 if there are none,
                          NOT rounded)

In the main block: read a line of text, call analyze_text(), and print a
summary. Round the average to 2 decimals when printing.

Example run:
    Enter text: I have 3 apples and 5 pears
    Characters (no spaces): 21
    Words: 7
    Numbers: [3, 5]
    Sum: 8
    Average: 4.00

Examples (these are also used to check your work):
>>> count_characters("a b  c")
3
>>> count_words("I have 3 apples and 5 pears")
7
>>> extract_numbers("Scores: 10, -4 and 7! but not 3.5 or abc123")
[10, -4, 7]
>>> result = analyze_text("I have 3 apples and 5 pears")
>>> result["characters"], result["words"], result["numbers"]
(21, 7, [3, 5])
>>> result["sum"], result["average"]
(8, 4.0)
>>> analyze_text("no numbers here")["average"]
0.0
"""


def count_characters(text: str) -> int:
    """Count characters that are not whitespace."""
    # Count all characters except whitespace
    return sum(1 for char in text if not char.isspace())


def count_words(text: str) -> int:
    """Count number of whitespace-separated words."""
    # Split the text into words and count them
    return len(text.split())


def extract_numbers(text: str) -> list[int]:
    """Return a list of the integers found in text, in order."""
    # Create an empty list to store the numbers
    numbers = []

    # Go through each word in the text
    for word in text.split():
        # Remove punctuation from the end of the word
        word = word.rstrip(".,!?;:")

        # Check if the word is a positive integer
        if word.isdigit():
            numbers.append(int(word))

        # Check if the word is a negative integer
        elif word.startswith("-") and word[1:].isdigit():
            numbers.append(int(word))

    # Return the list of extracted numbers
    return numbers


def analyze_text(text: str) -> dict:
    """Return a dict with characters, words, numbers, sum and average."""
    # Call the helper functions to analyze the text
    characters = count_characters(text)
    words = count_words(text)
    numbers = extract_numbers(text)

    # Calculate the sum of all extracted numbers
    total = sum(numbers)

    # Calculate the average, or use 0.0 if there are no numbers
    if numbers:
        average = total / len(numbers)
    else:
        average = 0.0

    # Return all results in a dictionary with exactly five keys
    return {
        "characters": characters,
        "words": words,
        "numbers": numbers,
        "sum": total,
        "average": average
    }


if __name__ == "__main__":
    # Read a line of text from the user
    text = input("Enter text: ")

    # Analyze the text using the main function
    result = analyze_text(text)

    # Print the summary
    print(f"Characters (no spaces): {result['characters']}")
    print(f"Words: {result['words']}")
    print(f"Numbers: {result['numbers']}")
    print(f"Sum: {result['sum']}")
    print(f"Average: {result['average']:.2f}")
