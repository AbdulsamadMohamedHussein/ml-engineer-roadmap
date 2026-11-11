"""Day 3: dictionaries, sets, list comprehensions.

Fill in each function (replace `pass`), then run this file.
The checks at the bottom tell you which ones pass.
"""

# QUICK PRIMER
# dict:   ages = {"Ali": 20}; ages["Sara"] = 22; ages.get("Omar", 0)
# set:    set([3, 1, 3]) -> {1, 3}   (no duplicates)
# comp:   [n * 2 for n in nums if n > 0]
# loop:   for key, value in my_dict.items():


def word_count(text):
    """Return a dict of how many times each word appears.
    word_count("the cat the dog") -> {"the": 2, "cat": 1, "dog": 1}
    Hint: text.split(), then loop and use dict.get(word, 0) + 1
    """
    pass


def most_common_word(text):
    """Return the word that appears most often.
    most_common_word("a b b c b a") -> "b"
    Hint: reuse word_count, then look for the biggest value.
    """
    pass


def unique_sorted(numbers):
    """Remove duplicates and sort.
    unique_sorted([3, 1, 3, 2, 1]) -> [1, 2, 3]
    Hint: set() then sorted()
    """
    pass


def squares_of_evens(numbers):
    """Return squares of the even numbers only, using a list comprehension.
    squares_of_evens([1, 2, 3, 4, 5, 6]) -> [4, 16, 36]
    """
    pass


def is_palindrome(text):
    """True if text reads the same backwards, ignoring spaces and case.
    is_palindrome("A man a plan a canal Panama") -> True
    """
    pass


def average_grades(grades):
    """Return a dict of each student's average.
    average_grades({"Ali": [80, 90], "Sara": [70, 100, 85]})
    -> {"Ali": 85.0, "Sara": 85.0}
    """
    pass


def check(name, got, expected):
    status = "PASS" if got == expected else "FAIL"
    print(f"{status}  {name}")
    if status == "FAIL":
        print(f"      got:      {got}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("word_count", word_count("the cat the dog"), {"the": 2, "cat": 1, "dog": 1})
    check("most_common_word", most_common_word("a b b c b a"), "b")
    check("unique_sorted", unique_sorted([3, 1, 3, 2, 1]), [1, 2, 3])
    check("squares_of_evens", squares_of_evens([1, 2, 3, 4, 5, 6]), [4, 16, 36])
    check("is_palindrome yes", is_palindrome("A man a plan a canal Panama"), True)
    check("is_palindrome no", is_palindrome("hello"), False)
    check("average_grades",
          average_grades({"Ali": [80, 90], "Sara": [70, 100, 85]}),
          {"Ali": 85.0, "Sara": 85.0})
