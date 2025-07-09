import re
import os
import time
import warnings
import logging.handlers # Explicitly import the handlers module, if needed for other parts of a larger script

"""
--- Python's `re` Module: Complete Guide and Code Examples ---

The `re` module in Python provides support for regular expressions (regex).
Regular expressions are powerful tools for pattern matching and manipulation of strings.
They allow you to define complex search patterns and perform operations like searching,
replacing, and splitting text based on these patterns.

### Why Use Regular Expressions?
* Powerful Pattern Matching: Go beyond simple substring searches. Match complex patterns
  like email addresses, phone numbers, dates, or specific code structures.
* Data Validation: Validate user input (e.g., ensuring a password meets certain criteria,
  or an email is in a valid format).
* Text Processing: Extract specific information from logs, parse configuration files,
  or clean up messy text data.
* Text Manipulation: Find and replace text based on patterns, or split strings using
  complex delimiters.

### Basic Concepts
* Pattern: The regular expression itself, defined as a string.
* String: The text you want to search within.
* Match Object: If a match is found, `re` functions return a match object, which contains
  information about the match (e.g., the matched string, its start and end positions,
  captured groups). If no match is found, `None` is returned.

### Key Functions in `re` Module

1.  `re.match(pattern, string, flags=0)`:
    * Attempts to match the `pattern` only at the **beginning** of the `string`.
    * Returns a match object if successful, `None` otherwise.

2.  `re.search(pattern, string, flags=0)`:
    * Scans through the `string` looking for the **first location** where the `pattern`
      produces a match.
    * Returns a match object if successful, `None` otherwise.

3.  `re.findall(pattern, string, flags=0)`:
    * Finds **all non-overlapping matches** of the `pattern` in the `string`.
    * Returns a list of strings if no capturing groups are used, or a list of tuples
      if multiple capturing groups are used.

4.  `re.finditer(pattern, string, flags=0)`:
    * Finds **all non-overlapping matches** of the `pattern` in the `string`.
    * Returns an **iterator** yielding match objects for each match. This is memory-efficient
      for large strings.

5.  `re.sub(pattern, repl, string, count=0, flags=0)`:
    * Replaces occurrences of the `pattern` in the `string` with `repl`.
    * `repl` can be a string or a function.
    * `count` specifies the maximum number of pattern occurrences to be replaced.
      `0` (default) means all occurrences.
    * Returns the modified string.

6.  `re.subn(pattern, repl, string, count=0, flags=0)`:
    * Similar to `re.sub()`, but returns a **tuple** `(new_string, number_of_substitutions_made)`.

7.  `re.split(pattern, string, maxsplit=0, flags=0)`:
    * Splits the `string` by occurrences of the `pattern`.
    * `maxsplit` specifies the maximum number of splits to perform. `0` (default) means all occurrences.
    * Returns a list of strings. If capturing parentheses are used in the pattern, then the text of
      all groups in the pattern are also returned as part of the result list.

8.  `re.compile(pattern, flags=0)`:
    * Compiles a regular expression `pattern` into a regex object.
    * This is useful when you need to use the same pattern multiple times, as it improves
      performance by pre-compiling the pattern. The compiled object has methods like
      `match()`, `search()`, `findall()`, etc.

### Regular Expression Syntax (Metacharacters and Special Sequences)

Regular expressions use special characters (metacharacters) and sequences to define patterns.

#### Metacharacters
* `.` (Dot): Matches any single character except newline (unless `re.DOTALL` flag is used).
* `^` (Caret): Matches the beginning of the string (or the beginning of a line if `re.MULTILINE` is used).
* `$` (Dollar): Matches the end of the string (or the end of a line if `re.MULTILINE` is used).
* `*` (Asterisk): Matches 0 or more occurrences of the preceding character/group. (Greedy)
* `+` (Plus): Matches 1 or more occurrences of the preceding character/group. (Greedy)
* `?` (Question Mark): Matches 0 or 1 occurrence of the preceding character/group. (Greedy) Also makes a quantifier non-greedy.
* `{m}`: Matches exactly `m` occurrences of the preceding character/group.
* `{m,n}`: Matches between `m` and `n` occurrences of the preceding character/group.
* `[]` (Square Brackets): Defines a character set. Matches any one character within the set.
    * `[abc]` matches 'a', 'b', or 'c'.
    * `[a-z]` matches any lowercase letter.
    * `[0-9]` matches any digit.
    * `[^abc]` matches any character *except* 'a', 'b', or 'c'. (Negation)
* `\` (Backslash): Escapes special characters (e.g., `\.` matches a literal dot). Also used for special sequences.
* `|` (Pipe): Acts as an OR operator. `cat|dog` matches "cat" or "dog".
* `()` (Parentheses): Creates a capturing group. Matches the enclosed pattern and captures the matched text.
  Also used for grouping parts of a pattern.

#### Special Sequences
* `\d`: Matches any digit (0-9). Equivalent to `[0-9]`.
* `\D`: Matches any non-digit character. Equivalent to `[^0-9]`.
* `\w`: Matches any word character (alphanumeric characters and underscore: `a-zA-Z0-9_`).
* `\W`: Matches any non-word character.
* `\s`: Matches any whitespace character (space, tab, newline, carriage return, form feed).
* `\S`: Matches any non-whitespace character.
* `\b`: Matches a word boundary. The position between a word character and a non-word character.
* `\B`: Matches a non-word boundary.
* `\A`: Matches the beginning of the string only (unlike `^` which can match line beginnings with `re.MULTILINE`).
* `\Z`: Matches the end of the string only (unlike `$` which can match line endings with `re.MULTILINE`).

### Quantifiers (Greedy vs. Non-Greedy)
By default, quantifiers (`*`, `+`, `?`, `{m,n}`) are **greedy**, meaning they try to match as much text as possible.
To make them **non-greedy** (or lazy), append a `?` after the quantifier:
* `*?`: Matches 0 or more, but as few as possible.
* `+?`: Matches 1 or more, but as few as possible.
* `??`: Matches 0 or 1, but as few as possible.
* `{m,n}?`: Matches between `m` and `n`, but as few as possible.

### Groups
Parentheses `()` create groups.
* Capturing Groups: `(pattern)` - Matches the pattern and captures the matched text. You can retrieve
  these captured parts using `match_object.group(n)` or `match_object.groups()`.
* Non-Capturing Groups: `(?:pattern)` - Matches the pattern but does not capture the text.
  Useful for grouping without adding to the captured groups list.
* Named Groups: `(?P<name>pattern)` - Matches the pattern and captures it, allowing you to refer to
  it by `name` (e.g., `match_object.group('name')`).

### Flags
Flags modify the behavior of the regular expression engine. They are passed as an optional argument
to `re` functions or `re.compile()`.
* `re.IGNORECASE` or `re.I`: Performs case-insensitive matching.
* `re.MULTILINE` or `re.M`: Makes `^` and `$` match the start/end of each line, not just the start/end of the string.
* `re.DOTALL` or `re.S`: Makes `.` match any character, including newline characters.
* `re.VERBOSE` or `re.X`: Allows you to write more readable regex by ignoring whitespace and allowing comments
  within the pattern.
* `re.ASCII` or `re.A`: Makes `\w`, `\W`, `\b`, `\B`, `\d`, `\D`, `\s`, `\S` perform ASCII-only matching.
* `re.LOCALE` or `re.L`: (Deprecated in Python 3.6+) Makes `\w`, `\W`, `\b`, `\B`, `\s`, `\S` dependent on the current locale.

### Lookarounds
Lookarounds assert that a pattern exists (or doesn't exist) without consuming characters.
They are zero-width assertions.
* Positive Lookahead: `(?=pattern)` - Asserts that `pattern` occurs immediately after the current position.
* Negative Lookahead: `(?!pattern)` - Asserts that `pattern` does *not* occur immediately after the current position.
* Positive Lookbehind: `(?<=pattern)` - Asserts that `pattern` occurs immediately before the current position.
* Negative Lookbehind: `(?<!pattern)` - Asserts that `pattern` does *not* occur immediately before the current position.

### Conditional Expressions (Less Common)
`(?(id/name)yes-pattern|no-pattern)` - Matches `yes-pattern` if the group with `id` or `name` exists,
otherwise matches `no-pattern`.
"""

# --- Global Cleanup Function (from previous logging example, included for completeness) ---
def clean_log_files(*filenames):
    """Removes specified log files if they exist."""
    for filename in filenames:
        if os.path.exists(filename):
            os.remove(filename)
            print(f"Cleaned up: {filename}")

print("--- Python re Module: All Scenarios Code Examples ---\n")

# --- 1. Basic re.match() ---
# re.match() checks for a match only at the beginning of the string.
print("1. re.match():")
text = "Hello, world!"
pattern = r"Hello" # 'r' prefix for raw string to avoid issues with backslashes
match_obj = re.match(pattern, text)
if match_obj:
    print(f"  Match found: '{match_obj.group()}' at position {match_obj.start()}-{match_obj.end()}")
else:
    print("  No match found at the beginning.")

text_no_start = "  Hello, world!"
match_obj_no_start = re.match(pattern, text_no_start)
if match_obj_no_start:
    print(f"  Match found: '{match_obj_no_start.group()}'")
else:
    print("  No match found at the beginning (due to leading spaces).")
print("-" * 30)

# --- 2. Basic re.search() ---
# re.search() scans the entire string for the first match.
print("2. re.search():")
text = "The quick brown fox jumps over the lazy dog."
pattern = r"fox"
search_obj = re.search(pattern, text)
if search_obj:
    print(f"  Search found: '{search_obj.group()}' at position {search_obj.start()}-{search_obj.end()}")
else:
    print("  No match found.")

pattern_not_found = r"cat"
search_obj_not_found = re.search(pattern_not_found, text)
if search_obj_not_found:
    print(f"  Search found: '{search_obj_not_found.group()}'")
else:
    print("  'cat' not found in the text.")
print("-" * 30)

# --- 3. Basic re.findall() ---
# re.findall() returns a list of all non-overlapping matches.
print("3. re.findall():")
text = "apple banana apple orange apple"
pattern = r"apple"
all_matches = re.findall(pattern, text)
print(f"  All 'apple' matches: {all_matches}")

# With capturing groups, it returns a list of tuples
text_emails = "user1@example.com, user2@domain.org, test@mail.net"
pattern_emails = r"(\w+)@(\w+\.\w+)"
all_email_parts = re.findall(pattern_emails, text_emails)
print(f"  All email parts (username, domain): {all_email_parts}")
print("-" * 30)

# --- 4. Basic re.finditer() ---
# re.finditer() returns an iterator yielding match objects.
print("4. re.finditer():")
text = "The rain in Spain falls mainly on the plain."
pattern = r"ain"
print("  Matches for 'ain':")
for match in re.finditer(pattern, text):
    print(f"    Found '{match.group()}' at {match.span()}")
print("-" * 30)

# --- 5. re.sub() and re.subn() ---
# Substitution operations.
print("5. re.sub() and re.subn():")
text = "Color, colour, favorite, favourite"
pattern_us = r"colour"
pattern_uk = r"favourite"

# Simple string replacement
new_text_color = re.sub(pattern_us, "color", text)
print(f"  'colour' to 'color': {new_text_color}")

# Using a function for replacement
def replace_vowel_with_x(match):
    """Replaces a matched vowel with 'x' characters of the same length."""
    return 'x' * len(match.group())

text_vowels = "hello world"
# Replace all vowels with 'x' of the same length
new_text_vowels = re.sub(r"[aeiou]", replace_vowel_with_x, text_vowels)
print(f"  Vowels replaced by 'x': {new_text_vowels}")

# re.subn() returns (new_string, count)
new_text_fav, count_fav = re.subn(pattern_uk, "favorite", text)
print(f"  'favourite' to 'favorite': {new_text_fav}, {count_fav} replacements.")
print("-" * 30)

# --- 6. re.split() ---
# Splitting strings by a regex pattern.
print("6. re.split():")
text = "one,two;three four"
# Split by comma, semicolon, or space
split_list_1 = re.split(r"[,;\s]", text)
print(f"  Split by [',', ';', ' ']: {split_list_1}")

text_with_delimiters = "apple:banana;cherry"
# If capturing groups are used, delimiters are also included in the result list
split_list_2 = re.split(r"(:|;)", text_with_delimiters)
print(f"  Split with capturing delimiters: {split_list_2}")

# maxsplit argument
split_list_3 = re.split(r"\s", "a b c d e", maxsplit=3)
print(f"  Split with maxsplit=2: {split_list_3}")
print("-" * 30)

# --- 7. re.compile() ---
# Compiling a regex for efficiency when used multiple times.
print("7. re.compile():")
compiled_pattern = re.compile(r"\d+") # Match one or more digits
text_numbers = "Item 10, Price 25.50, Quantity 3"
found_numbers = compiled_pattern.findall(text_numbers)
print(f"  Compiled pattern found numbers: {found_numbers}")

# Using compiled pattern for search
search_result = compiled_pattern.search("No numbers here, but 123 is a number.")
if search_result:
    print(f"  Compiled pattern search found: {search_result.group()}")
print("-" * 30)

# --- 8. Metacharacters and Special Sequences ---
print("8. Metacharacters and Special Sequences:")
text = "My phone number is 123-456-7890. Call me at 987.654.3210."

# . (dot) - matches any character (except newline)
print(f"  '.': {re.findall(r'a.l', 'apple, ball, tall')}") # Matches 'all' in ball, tall

# ^ (caret) - start of string
print(f"  '^': {re.search(r'^My', text).group() if re.search(r'^My', text) else 'No match'}")

# $ (dollar) - end of string
print(f"  '$': {re.search(r'3210.$', text).group() if re.search(r'3210.$', text) else 'No match'}") # Matches 3210.

# * (zero or more)
print(f"  '*': {re.findall(r'ab*c', 'ac abc abbc abbbc')}") # ac, abc, abbc, abbbc

# + (one or more)
print(f"  '+': {re.findall(r'ab+c', 'ac abc abbc abbbc')}") # abc, abbc, abbbc (no ac)

# ? (zero or one)
print(f"  '?': {re.findall(r'colou?r', 'color colour')}") # color, colour

# {m,n} (quantifiers)
pattern = r'\d{3}-\d{4}'  # Correct pattern

# Use f-string safely
print(f"  '{{m,n}}': {re.findall(pattern, text)}")
# [] (character set)
print(f"  '[]': {re.findall(r'[aeiou]', 'hello world')}") # All vowels

# [^] (negated character set)
print(f"  '[^]': {re.findall(r'[^aeious]', 'hello world')}") # Non-vowels, non-whitespace

# \d (digit), \D (non-digit)
re.findall(r'\\d+', text) # All numbers
pattern1 = r'\\D+'
print(f"  '\\D': {re.findall(pattern1, text)}") # All non-numbers

# \w (word char), \W (non-word char)
pattern1 =r'\\w+'
print(f"  '\\w': {re.findall(pattern1, text)}") # All words
print(f"  '\\W': {re.findall(pattern1, text)}") # All non-word characters

# \s (whitespace), \S (non-whitespace)
pattern = r'\\s'
print(f"  '\\s': {re.findall(pattern, text)}") # All spaces
print(f"  '\\S': {re.findall(pattern, text)}") # All non-whitespace blocks

# \b (word boundary)
pattern = r'\\bCall\\b'
print(f"  '\\b': {re.findall(pattern, text)}") # Matches 'Call' as a whole word

# \B (non-word boundary)
pattern = r'ing\\B'
print(f"  '\\B': {re.findall(pattern, 'singing, string, king')}") # Matches 'ing' in singing, string but not king

# \A (start of string)
pattern = r'\\AMy'
print(f"  '\\A': {re.search(pattern, text).group() if re.search(pattern, text) else 'No match'}")

# \Z (end of string)
pattern = r'3210.\\Z'
print(f"  '\\Z': {re.search(pattern, text).group() if re.search(pattern, text) else 'No match'}")
print("-" * 30)

# --- 9. Flags ---
print("9. Flags:")
text_flags = "Hello World\nhello python\nWORLD"

# re.IGNORECASE (re.I)
print(f"  re.I: {re.findall(r'hello', text_flags, re.I)}") # Matches Hello, hello

# re.MULTILINE (re.M) - ^ and $ match line start/end
print(f"  re.M (^): {re.findall(r'^hello', text_flags, re.M)}") # Matches 'hello' on the second line
print(f"  re.M ($): {re.findall(r'world$', text_flags, re.M | re.I)}") # Matches 'World' and 'WORLD'

# re.DOTALL (re.S) - . matches newline
text_dotall = "Line 1\nLine 2"
print(f"  re.S: {re.findall(r'Line.Line', text_dotall, re.S)}") # Matches "Line 1\nLine 2"

# re.VERBOSE (re.X) - allows comments and whitespace in pattern
pattern_verbose = re.compile(r"""
    ^(\d{3})        # Area code (3 digits)
    [\s.-]?         # Optional separator
    (\d{3})         # Middle 3 digits
    [\s.-]?         # Optional separator
    (\d{4})$        # Last 4 digits
""", re.X)
phone_number = "123-456-7890"
match_phone = pattern_verbose.match(phone_number)
if match_phone:
    print(f"  re.X (verbose): Phone number parts: {match_phone.groups()}")
print("-" * 30)

# --- 10. Greedy vs. Non-Greedy Quantifiers ---
print("10. Greedy vs. Non-Greedy Quantifiers:")
html_text = "<b>This is bold</b> and <i>this is italic</i>."

# Greedy: Matches as much as possible
greedy_pattern = r"<.*>"
print(f"  Greedy (.*): {re.findall(greedy_pattern, html_text)}") # Matches the whole string from first '<' to last '>'

# Non-Greedy (Lazy): Matches as little as possible
non_greedy_pattern = r"<.*?>"
print(f"  Non-Greedy (.*?): {re.findall(non_greedy_pattern, html_text)}") # Matches <b> and <i> separately
print("-" * 30)

# --- 11. Groups (Capturing, Non-Capturing, Named) ---
print("11. Groups:")
text_groups = "Name: John Doe, Age: 30, City: New York"

# Capturing Groups ()
pattern_capture = r"Name: (\w+ \w+), Age: (\d+)"
match_capture = re.search(pattern_capture, text_groups)
if match_capture:
    print(f"  Capturing Groups: Full match='{match_capture.group(0)}', Name='{match_capture.group(1)}', Age='{match_capture.group(2)}'")
    print(f"  All captured groups: {match_capture.groups()}")

# Non-Capturing Groups (?:)
# Grouping without capturing
pattern_non_capture = r"(?:Name): (\w+ \w+)"
match_non_capture = re.search(pattern_non_capture, text_groups)
if match_non_capture:
    print(f"  Non-Capturing Group: Name='{match_non_capture.group(1)}'") # group(0) is full match, group(1) is the first capturing group

# Named Groups (?P<name>...)
pattern_named = r"Name: (?P<full_name>\w+ \w+), Age: (?P<person_age>\d+)"
match_named = re.search(pattern_named, text_groups)
if match_named:
    print(f"  Named Groups: Full name='{match_named.group('full_name')}', Age='{match_named.group('person_age')}'")
    print(f"  Named groups dict: {match_named.groupdict()}")
print("-" * 30)

# --- 12. Lookarounds (Zero-Width Assertions) ---
print("12. Lookarounds:")
text_lookaround = "apple pie, pineapple, banana, orange juice"

# Positive Lookahead (?=...) - Match 'apple' only if followed by ' pie'
print(f"  Positive Lookahead (?=): {re.findall(r'apple(?= pie)', text_lookaround)}") # Matches 'apple'

# Negative Lookahead (?!...) - Match 'apple' only if NOT followed by ' pie'
print(f"  Negative Lookahead (?!): {re.findall(r'apple(?! pie)', text_lookaround)}") # Matches 'apple' in 'pineapple'

# Positive Lookbehind (?<=...) - Match 'pie' only if preceded by 'apple '
print(f"  Positive Lookbehind (?<=): {re.findall(r'(?<=apple )pie', text_lookaround)}") # Matches 'pie'

# Negative Lookbehind (?<!...) - Match 'apple' only if NOT preceded by 'pine'
print(f"  Negative Lookbehind (?<!): {re.findall(r'(?<!pine)apple', text_lookaround)}") # Matches 'apple' in 'apple pie'
print("-" * 30)

# --- 13. Conditional Expressions (Advanced) ---
# (?(id/name)yes-pattern|no-pattern) - Matches yes-pattern if group exists, else no-pattern
# This is less commonly used and can often be achieved with multiple regex or logic.
# Example: Match a date with optional year, but if year is present, it must be 4 digits.
print("13. Conditional Expressions (Advanced):")
# The conditional expression checks if a *previous* capturing group matched.
# A common use case is for optional parts that depend on another part's presence.
# For simplicity, let's stick to a basic demonstration of the syntax.

# Example: Match 'color' or 'colour', and if 'colour' was used, also match a specific suffix.
# This pattern is simplified for demonstration and may not cover all edge cases
# for complex conditional regex, which often leads to more readable code
# when handled with explicit Python logic.
text_conditional = "The colour is red. The color is blue."
# Match "colour" followed by " is red" if "colour" was matched (group 1).
# Otherwise (if "color" was matched), just match "color".
# Note: This is a complex regex feature and often simpler with multiple regex or Python logic.
pattern_conditional = re.compile(r"(colour)?(color)?(?P<suffix>(?(1) is red| is blue))")

match1 = pattern_conditional.search(text_conditional)
if match1:
    print(f"  Conditional match 1: {match1.group(0)}") # Should match 'colour is red'

text_conditional_2 = "The color is blue."
match2 = pattern_conditional.search(text_conditional_2)
if match2:
    print(f"  Conditional match 2: {match2.group(0)}") # Should match 'color is blue'
else:
    print("  Conditional match 2: No match found.")

print("  Conditional expressions are advanced and often handled with code logic for clarity.")
print("-" * 30)

# --- 14. Error Handling: Invalid Regex ---
print("14. Error Handling: Invalid Regex:")
try:
    # Unclosed parenthesis
    re.compile(r"\(").search("test")
except re.error as e:
    print(f"  Caught regex error for '(': {e}")

try:
    # Invalid escape sequence (e.g., \q is not a known sequence)
    re.search(r"q", "test")
except re.error as e:
    print(f"  Caught regex error for '\\q': {e}")
print("-" * 30)

# --- 15. Capturing Warnings (from previous logging example, included for completeness) ---
# Direct warnings issued by the `warnings` module to the logging system.
# Note: This requires the `logging` module to be configured.
# For this standalone script, it won't output to a log file unless logging is set up.
# If you run this as part of a larger script with logging configured, warnings will appear there.
print("\n--- Testing Capturing Warnings (requires logging setup) ---")
# Example of basic logging setup for warnings to be visible in console
# If you integrate this into a larger system, ensure your main logging setup handles this.
import logging
logging.basicConfig(level=logging.WARNING, format='%(asctime)s - %(levelname)s - %(message)s')
logging.captureWarnings(True) # Direct warnings to the logging system

# Issue a warning using the warnings module
warnings.warn("This is a warning from the warnings module!", UserWarning)
warnings.warn("Another warning that should appear in logs.", DeprecationWarning)

# Reset captureWarnings to default (False) if needed
# logging.captureWarnings(False)
print("-" * 30)


print("\n--- End of re Module Examples ---")
