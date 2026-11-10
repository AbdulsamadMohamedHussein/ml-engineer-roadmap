"""Day 2: Python functions and lists."""


def is_even(n):
    return n % 2 == 0


def average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


def count_vowels(text):
    return sum(1 for ch in text.lower() if ch in "aeiou")


def max_of_list(numbers):
    largest = numbers[0]
    for n in numbers:
        if n > largest:
            largest = n
    return largest


def reverse_string(text):
    return text[::-1]


def fizzbuzz(limit=100):
    for i in range(1, limit + 1):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


def two_sum(numbers, target):
    """Return indices of two numbers that add up to target, or None."""
    seen = {}  # value -> index
    for i, n in enumerate(numbers):
        needed = target - n
        if needed in seen:
            return seen[needed], i
        seen[n] = i
    return None


if __name__ == "__main__":
    # Tests: if any assert fails, Python tells you which one
    assert is_even(4) is True
    assert is_even(7) is False
    assert average([2, 4, 6]) == 4
    assert average([]) == 0
    assert count_vowels("Machine Learning") == 6
    assert max_of_list([3, 9, 2, 7]) == 9
    assert reverse_string("python") == "nohtyp"
    assert two_sum([2, 7, 11, 15], 9) == (0, 1)
    assert two_sum([1, 2, 3], 100) is None
    print("All tests passed!")
    fizzbuzz(15)
