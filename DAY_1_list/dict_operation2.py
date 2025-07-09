import collections # For Counter, if needed, though not directly used in these examples
import json # For JSON-like data representation

print("--- Advanced Dictionary Use Cases ---")

# --- Use Case 10: Merging Dictionaries ---
# Problem: Combine two or more dictionaries into a single one.
# Functions/Methods: dict.update(), ** (unpacking operator), | (union operator - Python 3.9+)

print("--- Use Case 10: Merging Dictionaries ---")

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 20, 'c': 3}
dict3 = {'d': 4, 'e': 5}

# Example 10.1: Using dict.update() (modifies in place)
merged_update = dict1.copy() # Start with a copy if dict1 shouldn't be modified
merged_update.update(dict2)
print(f"Merged with update(): {merged_update}")
# Output: Merged with update(): {'a': 1, 'b': 20, 'c': 3}

# Example 10.2: Using ** (dictionary unpacking - creates new dict, last value for duplicate keys wins)
merged_unpacking = {**dict1, **dict2}
print(f"Merged with unpacking (**): {merged_unpacking}")
# Output: Merged with unpacking (**): {'a': 1, 'b': 20, 'c': 3}

# Example 10.3: Merging multiple dictionaries with unpacking
merged_multiple = {**dict1, **dict2, **dict3}
print(f"Merged multiple with unpacking: {merged_multiple}")
# Output: Merged multiple with unpacking: {'a': 1, 'b': 20, 'c': 3, 'd': 4, 'e': 5}

# Example 10.4: Using | (union operator - Python 3.9+, creates new dict, last value for duplicate keys wins)
merged_union = dict1 | dict2
print(f"Merged with union (|): {merged_union}")
# Output: Merged with union (|): {'a': 1, 'b': 20, 'c': 3}

# Corner Case: Order of merging matters for duplicate keys
dict_a = {'x': 1, 'y': 2}
dict_b = {'y': 20, 'z': 30}
merged_ab = {**dict_a, **dict_b} # 'y' from dict_b wins
merged_ba = {**dict_b, **dict_a} # 'y' from dict_a wins
print(f"Merged A then B: {merged_ab}") # Output: Merged A then B: {'x': 1, 'y': 20, 'z': 30}
print(f"Merged B then A: {merged_ba}") # Output: Merged B then A: {'x': 1, 'y': 2, 'z': 30}

print("\n") # Separator

# --- Use Case 11: Inverting Dictionaries ---
# Problem: Create a new dictionary where original values become keys and original keys become values.
# Functions/Methods: Dictionary comprehension

print("--- Use Case 11: Inverting Dictionaries ---")

original_dict = {'apple': 'fruit', 'carrot': 'vegetable', 'banana': 'fruit'}

# Example 11.1: Simple inversion (if values are unique and hashable)
inverted_dict_simple = {v: k for k, v in original_dict.items()}
print(f"Inverted (simple): {inverted_dict_simple}")
# Output: Inverted (simple): {'fruit': 'banana', 'vegetable': 'carrot'}
# Corner Case: Duplicate values - the last key encountered for a value will overwrite previous ones.
# 'apple' is lost because 'banana' also maps to 'fruit'.

# Example 11.2: Inverting with handling duplicate values (values become keys, keys become lists of values)
inverted_dict_multi_value = collections.defaultdict(list)
for k, v in original_dict.items():
    inverted_dict_multi_value[v].append(k)
print(f"Inverted (multi-value): {dict(inverted_dict_multi_value)}")
# Output: Inverted (multi-value): {'fruit': ['apple', 'banana'], 'vegetable': ['carrot']}

# Corner Case: Values must be hashable to become keys
try:
    unhashable_value_dict = {'key1': [1, 2], 'key2': [3, 4]}
    inverted_unhashable = {v: k for k, v in unhashable_value_dict.items()}
except TypeError as e:
    print(f"Error inverting with unhashable values: {e}")
# Output: Error inverting with unhashable values: unhashable type: 'list'

print("\n") # Separator

# --- Use Case 12: Filtering Dictionaries ---
# Problem: Create a new dictionary containing only items that satisfy a certain condition.
# Functions/Methods: Dictionary comprehension

print("--- Use Case 12: Filtering Dictionaries ---")

data = {'a': 10, 'b': 25, 'c': 5, 'd': 30, 'e': 15}

# Example 12.1: Filter by value
filtered_by_value = {k: v for k, v in data.items() if v > 15}
print(f"Filtered by value (>15): {filtered_by_value}")
# Output: Filtered by value (>15): {'b': 25, 'd': 30}

# Example 12.2: Filter by key
filtered_by_key = {k: v for k, v in data.items() if k in ['a', 'd', 'f']}
print(f"Filtered by key ('a', 'd', 'f'): {filtered_by_key}")
# Output: Filtered by key ('a', 'd', 'f'): {'a': 10, 'd': 30}

# Example 12.3: Filter with combined conditions
filtered_combined = {k: v for k, v in data.items() if v % 5 == 0 and k != 'b'}
print(f"Filtered by combined conditions: {filtered_combined}")
# Output: Filtered by combined conditions: {'c': 5, 'd': 30, 'e': 15}

print("\n") # Separator

# --- Use Case 13: Transforming Dictionary Values/Keys ---
# Problem: Apply a function or transformation to the values or keys of a dictionary.
# Functions/Methods: Dictionary comprehension

print("--- Use Case 13: Transforming Dictionary Values/Keys ---")

data = {'item1': 10, 'item2': 20, 'item3': 30}

# Example 13.1: Square all values
squared_values = {k: v**2 for k, v in data.items()}
print(f"Squared values: {squared_values}")
# Output: Squared values: {'item1': 100, 'item2': 400, 'item3': 900}

# Example 13.2: Convert keys to uppercase
uppercase_keys = {k.upper(): v for k, v in data.items()}
print(f"Uppercase keys: {uppercase_keys}")
# Output: Uppercase keys: {'ITEM1': 10, 'ITEM2': 20, 'ITEM3': 30}

# Example 13.3: Transform both keys and values
transformed_dict = {k.replace('item', 'product'): v * 2 for k, v in data.items()}
print(f"Transformed keys and values: {transformed_dict}")
# Output: Transformed keys and values: {'product1': 20, 'product2': 40, 'product3': 60}

# Corner Case: Key collision during transformation
# If transformation results in duplicate keys, the last one processed wins.
collision_data = {'name_first': 'Alice', 'name_last': 'Smith'}
transformed_collision = {k.replace('name_', ''): v for k, v in collision_data.items()}
print(f"Transformed with key collision: {transformed_collision}")
# Output: Transformed with key collision: {'first': 'Alice', 'last': 'Smith'}
# (No collision here, but if both transformed to 'name', one would be lost)

print("\n") # Separator

# --- Use Case 14: Simulating Set Operations on Keys ---
# Problem: Find common keys, unique keys, or keys present in one but not another.
# Functions/Methods: dict.keys() (which returns a set-like view), set operations (&, |, -, ^)

print("--- Use Case 14: Simulating Set Operations on Keys ---")

dict_a = {'apple': 1, 'banana': 2, 'cherry': 3}
dict_b = {'banana': 20, 'date': 4, 'elderberry': 5}

keys_a = dict_a.keys() # These are set-like views
keys_b = dict_b.keys()

# Example 14.1: Intersection (common keys)
common_keys = keys_a & keys_b
print(f"Common keys: {common_keys}") # Output: Common keys: {'banana'}

# Example 14.2: Union (all unique keys)
all_keys = keys_a | keys_b
print(f"All unique keys: {all_keys}") # Output: All unique keys: {'apple', 'banana', 'cherry', 'date', 'elderberry'}

# Example 14.3: Difference (keys in A but not B)
a_minus_b = keys_a - keys_b
print(f"Keys in A but not B: {a_minus_b}") # Output: Keys in A but not B: {'apple', 'cherry'}

# Example 14.4: Symmetric Difference (keys unique to A or B)
symmetric_diff = keys_a ^ keys_b
print(f"Keys unique to A or B: {symmetric_diff}") # Output: Keys unique to A or B: {'apple', 'cherry', 'date', 'elderberry'}

# Corner Case: Operations with non-set iterables (convert to set first)
list_of_keys = ['banana', 'fig']
# common_keys_with_list = keys_a & list_of_keys # This would raise TypeError
common_keys_with_list = keys_a & set(list_of_keys)
print(f"Common keys with a list: {common_keys_with_list}") # Output: Common keys with a list: {'banana'}
