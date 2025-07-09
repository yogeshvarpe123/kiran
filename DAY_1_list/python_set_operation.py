import collections # For general utility, though not strictly needed for basic set ops

print("--- Python Set Operations and Use Cases ---")

# --- 1. Basic Set Creation and Characteristics ---
# Problem: How to create sets and understand their fundamental properties.
# Functions/Methods: set(), {} (for non-empty sets)
# Characteristics: Unordered, unique elements, mutable (can add/remove elements)

print("\n--- 1. Basic Set Creation and Characteristics ---")

# Example 1.1: Creating sets
empty_set = set() # Use set() for an empty set, {} creates an empty dictionary
print(f"Empty set: {empty_set}")

numbers_set = {1, 2, 3, 4, 5} # Direct literal for non-empty set
print(f"Numbers set: {numbers_set}")

# Sets automatically remove duplicates
duplicates_list = [1, 2, 2, 3, 1, 4, 5, 3]
unique_set = set(duplicates_list)
print(f"Set from list with duplicates: {unique_set}") # Output: {1, 2, 3, 4, 5} (order not guaranteed)

mixed_types_set = {1, "hello", True, 3.14} # True is treated as 1
print(f"Mixed types set: {mixed_types_set}") # Output: {1, 2, 3.14, 'hello'} (order varies)

# Corner Case: {} creates an empty dictionary, not an empty set
curly_braces_empty = {}
print(f"Type of {{}}: {type(curly_braces_empty)}") # Output: <class 'dict'>

# Corner Case: Elements must be hashable
# Lists, dictionaries, and other sets are mutable, hence not hashable.
try:
    set_with_unhashable = {[1, 2], 3}
except TypeError as e:
    print(f"Error with unhashable element: {e}") # Output: Error with unhashable element: unhashable type: 'list'


# --- 2. Adding Elements to a Set ---
# Problem: How to add single elements or multiple elements to a set.
# Functions/Methods: add(), update()

print("\n--- 2. Adding Elements to a Set ---")

my_set = {1, 2, 3}

# Example 2.1: add(element) - Adds a single element. No effect if element already exists.
my_set.add(4)
print(f"After add(4): {my_set}") # Output: {1, 2, 3, 4} (order varies)
my_set.add(2) # Adding existing element has no effect
print(f"After add(2) again: {my_set}") # Output: {1, 2, 3, 4} (order varies)

# Example 2.2: update(iterable) - Adds multiple elements from an iterable.
my_set.update([5, 6, 1]) # Add 5, 6. 1 is already present.
print(f"After update([5, 6, 1]): {my_set}") # Output: {1, 2, 3, 4, 5, 6} (order varies)
my_set.update("abc") # Adds individual characters
print(f"After update('abc'): {my_set}") # Output: {1, 2, 3, 4, 5, 6, 'a', 'b', 'c'} (order varies)

# Corner Case: update() with non-hashable elements in iterable
try:
    my_set.update([[7, 8]])
except TypeError as e:
    print(f"Error updating with unhashable element: {e}") # Output: Error updating with unhashable element: unhashable type: 'list'


# --- 3. Removing Elements from a Set ---
# Problem: How to remove elements by value, or clear the entire set.
# Functions/Methods: remove(), discard(), pop(), clear()

print("\n--- 3. Removing Elements from a Set ---")

data_set = {10, 20, 30, 40, 50}

# Example 3.1: remove(element) - Removes element. Raises KeyError if not found.
data_set.remove(30)
print(f"After remove(30): {data_set}") # Output: {10, 20, 40, 50} (order varies)

# Corner Case: KeyError if element not found
try:
    data_set.remove(99)
except KeyError as e:
    print(f"Error removing non-existent element with remove(): {e}") # Output: Error removing non-existent element with remove(): 99

# Example 3.2: discard(element) - Removes element. No error if not found.
data_set.discard(20)
print(f"After discard(20): {data_set}") # Output: {10, 40, 50} (order varies)
data_set.discard(99) # No error, element not present
print(f"After discard(99) (no change): {data_set}") # Output: {10, 40, 50} (order varies)

# Example 3.3: pop() - Removes and returns an arbitrary element. Raises KeyError if set is empty.
popped_element = data_set.pop()
print(f"Popped element: {popped_element}") # Output: (e.g., 10)
print(f"Set after pop(): {data_set}") # Output: {40, 50} (order varies)

# Corner Case: KeyError if pop() from empty set
empty_set_pop = set()
try:
    empty_set_pop.pop()
except KeyError as e:
    print(f"Error popping from empty set: {e}") # Output: Error popping from empty set: pop from an empty set

# Example 3.4: clear() - Removes all elements from the set
data_set.clear()
print(f"After clear(): {data_set}") # Output: set()


# --- 4. Set Operations (Mathematical) ---
# Problem: Perform union, intersection, difference, and symmetric difference between sets.
# Functions/Methods: |, union(), &, intersection(), -, difference(), ^, symmetric_difference()
# Also issubset(), issuperset(), isdisjoint()

print("\n--- 4. Set Operations (Mathematical) ---")

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
set_c = {3, 9, 10}

# Example 4.1: Union (elements in A or B or both)
union_set_op = set_a | set_b
union_method = set_a.union(set_b)
print(f"Union (operator |): {union_set_op}") # Output: {1, 2, 3, 4, 5, 6, 7, 8} (order varies)
print(f"Union (method .union()): {union_method}") # Output: {1, 2, 3, 4, 5, 6, 7, 8} (order varies)
# Union with multiple sets
union_multiple = set_a.union(set_b, set_c)
print(f"Union (multiple): {union_multiple}") # Output: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10} (order varies)

# Example 4.2: Intersection (elements common to both)
intersection_set_op = set_a & set_b
intersection_method = set_a.intersection(set_b)
print(f"Intersection (operator &): {intersection_set_op}") # Output: {4, 5} (order varies)
print(f"Intersection (method .intersection()): {intersection_method}") # Output: {4, 5} (order varies)
# Intersection with multiple sets
intersection_multiple = set_a.intersection(set_b, set_c)
print(f"Intersection (multiple): {intersection_multiple}") # Output: {5} (order varies, if 5 was in all three)
# Corrected for example:
set_a_prime = {1, 2, 3, 4, 5, 7}
set_b_prime = {4, 5, 6, 7, 8}
set_c_prime = {3, 7, 9}
intersection_multiple_correct = set_a_prime.intersection(set_b_prime, set_c_prime)
print(f"Intersection (multiple, corrected): {intersection_multiple_correct}") # Output: {7}

# Example 4.3: Difference (elements in A but not B)
difference_set_op = set_a - set_b
difference_method = set_a.difference(set_b)
print(f"Difference (operator -): {difference_set_op}") # Output: {1, 2, 3} (order varies)
print(f"Difference (method .difference()): {difference_method}") # Output: {1, 2, 3} (order varies)

# Example 4.4: Symmetric Difference (elements in A or B, but not both)
symmetric_diff_set_op = set_a ^ set_b
symmetric_diff_method = set_a.symmetric_difference(set_b)
print(f"Symmetric Difference (operator ^): {symmetric_diff_set_op}") # Output: {1, 2, 3, 6, 7, 8} (order varies)
print(f"Symmetric Difference (method .symmetric_difference()): {symmetric_diff_method}") # Output: {1, 2, 3, 6, 7, 8} (order varies)

# Example 4.5: issubset(), issuperset(), isdisjoint()
set_small = {1, 2}
set_large = {1, 2, 3, 4}
set_other = {5, 6}

print(f"Is {set_small} a subset of {set_large}? {set_small.issubset(set_large)}") # Output: True
print(f"Is {set_large} a superset of {set_small}? {set_large.issuperset(set_small)}") # Output: True
print(f"Are {set_small} and {set_other} disjoint? {set_small.isdisjoint(set_other)}") # Output: True (no common elements)
print(f"Are {set_small} and {set_large} disjoint? {set_small.isdisjoint(set_large)}") # Output: False (common elements 1, 2)

# Corner Case: Set operations with other iterables (methods accept iterables, operators require sets)
list_b_as_iterable = [4, 5, 6, 7, 8]
# print(set_a | list_b_as_iterable) # This would raise TypeError
print(f"Union with list (method): {set_a.union(list_b_as_iterable)}") # Output: {1, 2, 3, 4, 5, 6, 7, 8} (order varies)


# --- 5. Other Utility Methods ---
# Problem: Get size, create copies.
# Functions/Methods: len(), copy()

print("\n--- 5. Other Utility Methods ---")

my_set_util = {10, 20, 30}

# Example 5.1: len() - Get the number of elements
print(f"Length of set: {len(my_set_util)}") # Output: 3

# Example 5.2: copy() - Create a shallow copy
copied_set = my_set_util.copy()
copied_set.add(40)
print(f"Original set: {my_set_util}") # Output: {10, 20, 30} (order varies)
print(f"Copied set: {copied_set}") # Output: {10, 20, 30, 40} (order varies)

# Corner Case: Sets only do shallow copies. If elements were mutable (which they can't be as keys),
# a deep copy would be needed for nested mutable structures, but sets only hold hashable items.
# So, this is less of a concern for sets than for lists/dicts.


# --- 6. Common Set Use Cases ---

print("\n--- 6. Common Set Use Cases ---")

# Example 6.1: Removing Duplicates from a List (most common use)
# Problem: Efficiently get unique elements from a list.
data_list_duplicates = [1, 5, 2, 8, 5, 1, 9, 2]
unique_elements = list(set(data_list_duplicates))
print(f"Original list: {data_list_duplicates}") # Output: [1, 5, 2, 8, 5, 1, 9, 2]
print(f"Unique elements (set conversion): {unique_elements}") # Output: [1, 2, 5, 8, 9] (order not guaranteed)

# Example 6.2: Fast Membership Testing (O(1) average time complexity)
# Problem: Check if an element exists in a collection very quickly.
large_data_set = set(range(1_000_000))
element_to_check = 500_000
print(f"Is {element_to_check} in large_data_set? {element_to_check in large_data_set}") # Output: True

# Corner Case: Checking for non-hashable items
# You can't directly check for a list in a set if the list itself is not hashable.
# You'd need to convert the item to a hashable type (e.g., tuple) if it matches the set's elements.
set_of_tuples = {(1,2), (3,4)}
print(f"Is (1,2) in set_of_tuples? {(1,2) in set_of_tuples}") # Output: True
try:
    print(f"Is [1,2] in set_of_tuples? {[1,2] in set_of_tuples}")
except TypeError as e:
    print(f"Error checking for unhashable item: {e}") # Output: Error checking for unhashable item: unhashable type: 'list'


# Example 6.3: Finding Common Elements between two lists
# Problem: Get elements that exist in both lists.
list_a = [1, 2, 3, 4, 5]
list_b = [4, 5, 6, 7, 8]
common = list(set(list_a) & set(list_b))
print(f"Common elements: {common}") # Output: [4, 5] (order not guaranteed)

# Example 6.4: Finding Unique Elements across multiple lists
# Problem: Get all distinct elements from several lists.
list_c = [1, 10, 11]
list_d = [10, 12, 13]
all_unique = list(set(list_a) | set(list_c) | set(list_d))
print(f"All unique elements: {all_unique}") # Output: [1, 2, 3, 4, 5, 10, 11, 12, 13] (order not guaranteed)

# Example 6.5: Identifying Differences (e.g., new, removed items)
# Problem: Compare two versions of a collection to see what changed.
old_users = {'Alice', 'Bob', 'Charlie'}
new_users = {'Bob', 'David', 'Eve'}

added_users = new_users - old_users
removed_users = old_users - new_users
common_users = old_users & new_users

print(f"Added users: {added_users}") # Output: {'David', 'Eve'}
print(f"Removed users: {removed_users}") # Output: {'Alice', 'Charlie'}
print(f"Common users: {common_users}") # Output: {'Bob'}

# Corner Case: Modifying a set while iterating over it (RuntimeError)
# Similar to dictionaries and lists, avoid this.
mod_set = {1, 2, 3}
try:
    for x in mod_set:
        if x == 1:
            mod_set.add(4) # Adding
        elif x == 2:
            mod_set.remove(3) # Removing
except RuntimeError as e:
    print(f"Error modifying set during iteration: {e}") # Output: Error modifying set during iteration: set changed size during iteration

