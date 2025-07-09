import collections # For Counter and defaultdict
import json # For JSON-like data

# --- Use Case 1: Counting Frequencies / Histograms ---
# Problem: Count the occurrences of items in a list or characters in a string.
# Functions/Methods: dict.get(), dict[key] for assignment, collections.Counter

print("--- Use Case 1: Counting Frequencies / Histograms ---")

# Example 1.1: Counting words in a sentence
sentence = "the quick brown fox jumps over the lazy dog the quick brown fox"
words = sentence.split()
word_counts = {}
for word in words:
    word_counts[word] = word_counts.get(word, 0) + 1 # Efficiently increments or initializes to 1
print(f"Word counts (manual): {word_counts}")
# Output: Word counts (manual): {'the': 3, 'quick': 2, 'brown': 2, 'fox': 2, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog': 1}

# Example 1.2: Using collections.Counter (more concise)
from collections import Counter
word_counts_counter = Counter(words)
print(f"Word counts (Counter): {word_counts_counter}")
# Output: Word counts (Counter): Counter({'the': 3, 'quick': 2, 'brown': 2, 'fox': 2, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog': 1})

# Corner Case: Counting with mixed case (normalize first)
mixed_case_words = ["Apple", "apple", "Banana", "apple"]
normalized_counts = {}
for word in mixed_case_words:
    normalized_word = word.lower()
    normalized_counts[normalized_word] = normalized_counts.get(normalized_word, 0) + 1
print(f"Normalized word counts: {normalized_counts}")
# Output: Normalized word counts: {'apple': 3, 'banana': 1}

print("\n") # Separator

# --- Use Case 2: Mapping Data / Lookups ---
# Problem: Store and retrieve data based on a unique identifier.
# Functions/Methods: dict[key], dict.get()

print("--- Use Case 2: Mapping Data / Lookups ---")

# Example 2.1: User profiles
user_profiles = {
    'user123': {'name': 'Alice', 'email': 'alice@example.com', 'status': 'active'},
    'user456': {'name': 'Bob', 'email': 'bob@example.com', 'status': 'inactive'}
}

# Lookup a user
user_id = 'user123'
if user_id in user_profiles:
    print(f"Profile for {user_id}: {user_profiles[user_id]}")
else:
    print(f"User {user_id} not found.")
# Output: Profile for user123: {'name': 'Alice', 'email': 'alice@example.com', 'status': 'active'}

# Example 2.2: Price lookup
product_prices = {
    'Laptop': 1200.00,
    'Mouse': 25.50,
    'Keyboard': 75.00
}
item = 'Mouse'
price = product_prices.get(item, "Price not available")
print(f"Price of {item}: ${price}")
# Output: Price of Mouse: $25.5

# Corner Case: Handling missing keys gracefully
item_missing = 'Monitor'
price_missing = product_prices.get(item_missing, "Item not in stock")
print(f"Price of {item_missing}: {price_missing}")
# Output: Price of Monitor: Item not in stock

print("\n") # Separator

# --- Use Case 3: Configuration Settings ---
# Problem: Store application configuration parameters.
# Functions/Methods: dict[key], dict.update(), dict.get()

print("--- Use Case 3: Configuration Settings ---")

app_config = {
    'database_url': 'sqlite:///app.db',
    'debug_mode': True,
    'log_level': 'INFO',
    'max_connections': 10
}

# Accessing a setting
print(f"Debug mode: {app_config['debug_mode']}")
# Output: Debug mode: True

# Updating a setting
app_config['log_level'] = 'DEBUG'
print(f"Updated log level: {app_config['log_level']}")
# Output: Updated log level: DEBUG

# Adding new settings or overriding defaults
default_config = {
    'timeout_seconds': 30,
    'cache_enabled': False,
    'log_level': 'WARNING' # Default for log_level
}
# Use update to apply new settings, existing keys are overwritten
app_config.update(default_config)
print(f"Config after update with defaults: {app_config}")
# Output: Config after update with defaults: {'database_url': 'sqlite:///app.db', 'debug_mode': True, 'log_level': 'WARNING', 'max_connections': 10, 'timeout_seconds': 30, 'cache_enabled': False}

print("\n") # Separator

# --- Use Case 4: Grouping Data ---
# Problem: Organize a list of items into groups based on a common attribute.
# Functions/Methods: collections.defaultdict, dict.setdefault(), list.append()

print("--- Use Case 4: Grouping Data ---")

students = [
    {'name': 'Alice', 'grade': 'A', 'major': 'CS'},
    {'name': 'Bob', 'grade': 'B', 'major': 'EE'},
    {'name': 'Charlie', 'grade': 'A', 'major': 'CS'},
    {'name': 'David', 'grade': 'C', 'major': 'ME'},
    {'name': 'Eve', 'grade': 'A', 'major': 'EE'}
]

# Example 4.1: Grouping by major (using defaultdict)
from collections import defaultdict
students_by_major = defaultdict(list) # Default value for new keys is an empty list
for student in students:
    students_by_major[student['major']].append(student['name'])
print(f"Students by major (defaultdict): {dict(students_by_major)}") # Convert back to dict for clean print
# Output: Students by major (defaultdict): {'CS': ['Alice', 'Charlie'], 'EE': ['Bob', 'Eve'], 'ME': ['David']}

# Example 4.2: Grouping by grade (using dict.setdefault)
students_by_grade = {}
for student in students:
    grade = student['grade']
    students_by_grade.setdefault(grade, []).append(student['name'])
print(f"Students by grade (setdefault): {students_by_grade}")
# Output: Students by grade (setdefault): {'A': ['Alice', 'Charlie', 'Eve'], 'B': ['Bob'], 'C': ['David']}

print("\n") # Separator

# --- Use Case 5: Caching / Memoization ---
# Problem: Store results of expensive function calls to avoid re-computing them.
# Functions/Methods: dict[key], dict.get()

print("--- Use Case 5: Caching / Memoization ---")

# Example 5.1: Simple Fibonacci with caching
fib_cache = {}
def fibonacci(n):
    if n <= 1:
        return n
    if n in fib_cache:
        return fib_cache[n] # Return from cache if available

    # Compute and store in cache
    result = fibonacci(n - 1) + fibonacci(n - 2)
    fib_cache[n] = result
    return result

print(f"Fibonacci(10): {fibonacci(10)}") # Output: Fibonacci(10): 55
print(f"Fibonacci cache: {fib_cache}") # Output: Fibonacci cache: {2: 1, 3: 2, 4: 3, 5: 5, 6: 8, 7: 13, 8: 21, 9: 34, 10: 55}

# Example 5.2: Using functools.lru_cache (built-in decorator)
from functools import lru_cache

@lru_cache(maxsize=128) # Cache up to 128 most recently used results
def fibonacci_lru(n):
    if n <= 1:
        return n
    return fibonacci_lru(n - 1) + fibonacci_lru(n - 2)

print(f"Fibonacci(10) with lru_cache: {fibonacci_lru(10)}") # Output: Fibonacci(10) with lru_cache: 55
# No direct access to the cache, but it's working behind the scenes
# print(fibonacci_lru.cache_info()) # Can inspect cache info

print("\n") # Separator

# --- Use Case 6: Representing Structured Data (JSON-like) ---
# Problem: Model hierarchical or complex data structures.
# Functions/Methods: Nested dictionaries, dict.get(), dict.items(), json module

print("--- Use Case 6: Representing Structured Data (JSON-like) ---")

# Example 6.1: Product catalog entry
product = {
    "id": "PROD001",
    "name": "Wireless Headphones",
    "category": "Electronics",
    "price": 99.99,
    "available": True,
    "specifications": {
        "color": ["Black", "White", "Blue"],
        "connectivity": "Bluetooth 5.0",
        "battery_life_hours": 20
    },
    "reviews": [
        {"user": "Alice", "rating": 5, "comment": "Great sound!"},
        {"user": "Bob", "rating": 4, "comment": "Comfortable, but battery could be better."}
    ]
}

# Accessing nested data
print(f"Product name: {product['name']}")
print(f"Available colors: {product['specifications']['color']}")
print(f"First review comment: {product['reviews'][0]['comment']}")

# Iterating through nested lists of dictionaries
print("All review comments:")
for review in product['reviews']:
    print(f"- {review['user']}: {review['comment']}")
# Output:
# - Alice: Great sound!
# - Bob: Comfortable, but battery could be better.

# Converting to JSON string
import json
json_string = json.dumps(product, indent=2)
print("\nProduct as JSON:")
print(json_string)

# Corner Case: Handling potentially missing nested keys
# Use .get() for safe navigation
battery_life = product.get('specifications', {}).get('battery_life_hours', 'N/A')
print(f"Battery life: {battery_life}") # Output: Battery life: 20

non_existent_spec = product.get('specifications', {}).get('weight_grams', 'Not specified')
print(f"Weight: {non_existent_spec}") # Output: Weight: Not specified

print("\n") # Separator

# --- Use Case 7: Sparse Data Representation ---
# Problem: Store data where many values are default or zero, saving memory.
# Functions/Methods: Dictionary itself (only store non-default values)

print("--- Use Case 7: Sparse Data Representation ---")

# Example 7.1: Sparse matrix row
# Imagine a row of a matrix where most elements are 0.
# Instead of [0, 0, 5, 0, 0, 0, 12, 0, 0], store only non-zero values.
sparse_row = {2: 5, 6: 12} # key is column index, value is non-zero element

def get_matrix_element(row_dict, index):
    return row_dict.get(index, 0) # Default to 0 if key not present

print(f"Element at index 2: {get_matrix_element(sparse_row, 2)}") # Output: Element at index 2: 5
print(f"Element at index 0: {get_matrix_element(sparse_row, 0)}") # Output: Element at index 0: 0

# Example 7.2: User preferences with defaults
# Only store preferences that differ from the global default
user_preferences = {
    'theme': 'dark',
    'notifications_enabled': True,
    'language': 'en'
}
global_defaults = {
    'theme': 'light',
    'notifications_enabled': True,
    'font_size': 14,
    'language': 'en'
}

def get_user_setting(user_prefs, setting_name, defaults):
    # User's specific setting takes precedence, otherwise use global default
    return user_prefs.get(setting_name, defaults.get(setting_name))

print(f"User's theme: {get_user_setting(user_preferences, 'theme', global_defaults)}") # Output: User's theme: dark
print(f"User's font size: {get_user_setting(user_preferences, 'font_size', global_defaults)}") # Output: User's font size: 14
print(f"User's notifications: {get_user_setting(user_preferences, 'notifications_enabled', global_defaults)}") # Output: User's notifications: True (from user_preferences)

print("\n") # Separator

# --- Use Case 8: Implementing Switch/Case Logic (Python 3.10+ with match/case) ---
# Problem: Execute different code blocks based on a key/value.
# Functions/Methods: dict.get() with functions/lambdas as values, or Python 3.10+ match/case

print("--- Use Case 8: Implementing Switch/Case Logic ---")

# Example 8.1: Using a dictionary to map actions (pre-Python 3.10)
def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b

operations = {
    'add': add,
    'subtract': subtract,
    'multiply': multiply
}

op_type = 'add'
num1, num2 = 10, 5

if op_type in operations:
    result = operations[op_type](num1, num2)
    print(f"Result of {op_type}: {result}") # Output: Result of add: 15
else:
    print("Invalid operation")

op_type = 'divide'
if op_type in operations:
    result = operations[op_type](num1, num2)
else:
    print(f"Result of {op_type}: Invalid operation") # Output: Result of divide: Invalid operation

# Example 8.2: Using match/case (Python 3.10+) - more readable for simple cases
# (This is a language construct, not a dict method, but often replaces dict-based switches)
def handle_command(command):
    match command:
        case "start":
            print("Starting service...")
        case "stop":
            print("Stopping service...")
        case "restart":
            print("Restarting service...")
        case _: # Default case
            print(f"Unknown command: {command}")

# handle_command("start")
# handle_command("status")

print("\n") # Separator

# --- Use Case 9: Removing Duplicates (Maintaining Order) ---
# Problem: Given a list with duplicates, get unique elements while preserving order.
# Functions/Methods: dict.fromkeys() (Python 3.7+ for order preservation)

print("--- Use Case 9: Removing Duplicates (Maintaining Order) ---")

my_list = [1, 2, 2, 3, 1, 4, 5, 3]

# Using dict.fromkeys() to get unique elements while preserving order (Python 3.7+)
unique_elements_ordered = list(dict.fromkeys(my_list))
print(f"Original list: {my_list}") # Output: Original list: [1, 2, 2, 3, 1, 4, 5, 3]
print(f"Unique elements (ordered): {unique_elements_ordered}") # Output: Unique elements (ordered): [1, 2, 3, 4, 5]

# Corner Case: Elements must be hashable
# If my_list contained mutable items like lists, this would fail.
# For example: list(dict.fromkeys([[1], [2], [1]])) would raise a TypeError.
