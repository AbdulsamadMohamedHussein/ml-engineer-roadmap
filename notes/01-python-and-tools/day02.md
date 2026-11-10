# Day 2: Python Functions and Git Branching

**Date:** 10 November 2026
**Phase:** 1, Python, Git, SQL
**Time spent:** ~90 minutes

## What I did
- Wrote 5 functions: `is_even`, `average`, `count_vowels`, `max_of_list`, `reverse_string`
- Solved FizzBuzz and Two Sum
- Practiced Git branching: create a branch, commit, merge, push
- Fixed a rejected push by pulling and merging remote changes

## Key concepts
| Concept | What it means | Example |
|:--|:--|:--|
| Function | Reusable block of code that takes input and returns output | `def is_even(n): return n % 2 == 0` |
| Modulo `%` | Remainder after division | `7 % 2 = 1` |
| List loop | Go through each item | `for n in numbers:` |
| Dictionary | Key-value lookup, very fast | `seen[n] = i` |
| `enumerate` | Gives index and value together | `for i, n in enumerate(nums)` |
| Slicing | Take part of a sequence | `text[::-1]` reverses a string |

## Code
See [`day02.py`](day02.py).

## What was hard
-

## What I learned
- Two Sum with a dictionary is one pass over the list instead of two nested loops, which is much faster on big lists.
- `git pull --allow-unrelated-histories` merges a repo that has separate histories.

## Questions I still have
-

## Next
- [ ] 3 more practice problems (lists and strings)
- [ ] Learn dictionaries and sets properly
- [ ] Read a file and count word frequencies
