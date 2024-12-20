def count_words(text):
    # remove leading and trailing spaces
    text = text.strip()

    # handle empty string
    if not text:
        return 0

    text = " ".join(text.split())

    return len(text.split())


test_cases = [
    "hello world",
    "  hello   world  ",
    "",
    "   ",
    "single",
    "Hello! How are you?",
]

for test in test_cases:
    print(f"Input: '{test}'")
    print(f"Word count: {count_words(test)}\n")
