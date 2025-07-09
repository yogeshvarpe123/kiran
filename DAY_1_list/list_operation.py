import copy # For deep copy operations
import collections # For deque and defaultdict
import itertools # For advanced flattening

print("--- Python List Operations and Use Cases ---")

# --- 1. Basic List Creation and Access ---
# Problem: How to create lists and access their elements.
# Functions/Methods: [], list(), indexing, slicing

print("\n--- 1. Basic List Creation and Access ---")

# Example 1.1: Creating lists
empty_list = []
print(f"Empty list: {empty_list}")

numbers = [1, 2, 3, 4, 5]
print(f"Numbers list: {numbers}")

mixed_types = [1, "hello", True, 3.14]
print(f"Mixed types list: {mixed_types}")

nested_list = [[1, 2], [3, 4], [5, 6]]
print(f"Nested list: {nested_list}")

# Example 1.2: Accessing elements (indexing)
print(f"First element of numbers: {numbers[0]}") # Output: 1
print(f"Last element of numbers: {numbers[-1]}") # Output: 5
print(f"Element from nested list: {nested_list[0][1]}") # Output: 2

# Corner Case: IndexError for out-of-bounds access
try:
    print(numbers[10])
except IndexError as e:
    print(f"Error accessing out of bounds: {e}") # Output: Error accessing out of bounds: list index out of range

# Example 1.3: Slicing lists
sub_list = numbers[1:4] # Elements from index 1 up to (but not including) 4
print(f"Slice [1:4]: {sub_list}") # Output: [2, 3, 4]
first_three = numbers[:3] # From start up to (but not including) 3
print(f"Slice [:3]: {first_three}") # Output: [1, 2, 3]
last_two = numbers[3:] # From index 3 to the end
print(f"Slice [3:]: {last_two}") # Output: [4, 5]
copy_list = numbers[:] # Creates a shallow copy
print(f"Slice [:]: {copy_list}") # Output: [1, 2, 3, 4, 5]
step_slice = numbers[::2] # Every second element
print(f"Slice [::2]: {step_slice}") # Output: [1, 3, 5]
reverse_slice = numbers[::-1] # Reverse the list
print(f"Slice [::-1]: {reverse_slice}") # Output: [5, 4, 3, 2, 1]

# Corner Case: Slicing an empty list
empty_slice = empty_list[1:3]
print(f"Slice of empty list: {empty_slice}") # Output: [] (no error)


# --- 2. Adding Elements to a List ---
# Problem: How to add single elements or multiple elements to a list.
# Functions/Methods: append(), insert(), extend(), + (concatenation)

print("\n--- 2. Adding Elements to a List ---")

my_list = [1, 2, 3]

# Example 2.1: append() - Adds a single element to the end
my_list.append(4)
print(f"After append(4): {my_list}") # Output: [1, 2, 3, 4]
my_list.append([5, 6]) # Appends the list as a single element
print(f"After append([5,6]): {my_list}") # Output: [1, 2, 3, 4, [5, 6]]

# Example 2.2: insert() - Adds an element at a specific index
my_list.insert(1, 99) # Insert 99 at index 1
print(f"After insert(1, 99): {my_list}") # Output: [1, 99, 2, 3, 4, [5, 6]]
my_list.insert(len(my_list), 100) # Insert at the end (same as append)
print(f"After insert(len, 100): {my_list}") # Output: [1, 99, 2, 3, 4, [5, 6], 100]
my_list.insert(1000, 101) # Corner Case: Index out of bounds (inserts at end)
print(f"After insert(1000, 101): {my_list}") # Output: [1, 99, 2, 3, 4, [5, 6], 100, 101]

# Example 2.3: extend() - Appends elements from an iterable
another_list = [10, 20]
my_list.extend(another_list)
print(f"After extend([10,20]): {my_list}") # Output: [1, 99, 2, 3, 4, [5, 6], 100, 101, 10, 20]
my_list.extend("abc") # Extends with individual characters
print(f"After extend('abc'): {my_list}") # Output: [1, 99, 2, 3, 4, [5, 6], 100, 101, 10, 20, 'a', 'b', 'c']

# Example 2.4: + operator (concatenation - creates a new list)
list_a = [1, 2]
list_b = [3, 4]
combined_list = list_a + list_b
print(f"Concatenated list: {combined_list}") # Output: [1, 2, 3, 4]
print(f"Original list_a (unchanged): {list_a}") # Output: Original list_a (unchanged): [1, 2]


# --- 3. Removing Elements from a List ---
# Problem: How to remove elements by value, by index, or clear the entire list.
# Functions/Methods: remove(), pop(), clear(), del statement

print("\n--- 3. Removing Elements from a List ---")

data_list = [10, 20, 30, 20, 40]

# Example 3.1: remove(value) - Removes the first occurrence of a value
data_list.remove(20)
print(f"After remove(20): {data_list}") # Output: [10, 30, 20, 40]

# Corner Case: ValueError if value not found
try:
    data_list.remove(99)
except ValueError as e:
    print(f"Error removing non-existent value: {e}") # Output: Error removing non-existent value: list.remove(x): x not in list

# Example 3.2: pop(index) - Removes and returns element at specified index (default last)
popped_last = data_list.pop() # Removes and returns last element
print(f"Popped last: {popped_last}") # Output: Popped last: 40
print(f"List after pop(): {data_list}") # Output: [10, 30, 20]

popped_at_index = data_list.pop(0) # Removes and returns element at index 0
print(f"Popped at index 0: {popped_at_index}") # Output: Popped at index 0: 10
print(f"List after pop(0): {data_list}") # Output: [30, 20]

# Corner Case: IndexError if index out of range for pop()
try:
    data_list.pop(10)
except IndexError as e:
    print(f"Error popping out of bounds: {e}") # Output: Error popping out of bounds: pop index out of range

# Example 3.3: clear() - Removes all items from the list
data_list.clear()
print(f"After clear(): {data_list}") # Output: []

# Example 3.4: del statement - Removes by index or slice
del_list = [1, 2, 3, 4, 5]
del del_list[1] # Delete element at index 1
print(f"After del del_list[1]: {del_list}") # Output: [1, 3, 4, 5]

del del_list[1:3] # Delete slice from index 1 up to (not including) 3
print(f"After del del_list[1:3]: {del_list}") # Output: [1, 5]

# Corner Case: IndexError for del out of bounds
try:
    del del_list[10]
except IndexError as e:
    print(f"Error deleting out of bounds with del: {e}") # Output: Error deleting out of bounds with del: list assignment index out of range


# --- 4. Searching and Counting Elements ---
# Problem: Find the index of an element or count its occurrences.
# Functions/Methods: index(), count()

print("\n--- 4. Searching and Counting Elements ---")

search_list = ['apple', 'banana', 'cherry', 'apple', 'date']

# Example 4.1: index(value, start, end) - Returns the index of the first occurrence
idx_banana = search_list.index('banana')
print(f"Index of 'banana': {idx_banana}") # Output: 1

idx_apple_after_0 = search_list.index('apple', 1) # Find 'apple' starting from index 1
print(f"Index of 'apple' after index 0: {idx_apple_after_0}") # Output: 3

# Corner Case: ValueError if value not found
try:
    search_list.index('grape')
except ValueError as e:
    print(f"Error finding non-existent value: {e}") # Output: Error finding non-existent value: 'grape' is not in list

# Example 4.2: count(value) - Returns the number of occurrences of a value
count_apple = search_list.count('apple')
print(f"Count of 'apple': {count_apple}") # Output: 2

count_orange = search_list.count('orange')
print(f"Count of 'orange': {count_orange}") # Output: 0


# --- 5. Sorting and Reversing Lists ---
# Problem: Arrange elements in a specific order or reverse their order.
# Functions/Methods: sort(), sorted(), reverse(), reversed()

print("\n--- 5. Sorting and Reversing Lists ---")

sort_list = [3, 1, 4, 1, 5, 9, 2]

# Example 5.1: sort() - Sorts the list in-place (modifies original list)
sort_list.sort()
print(f"After sort(): {sort_list}") # Output: [1, 1, 2, 3, 4, 5, 9]

sort_list.sort(reverse=True) # Sort in descending order
print(f"After sort(reverse=True): {sort_list}") # Output: [9, 5, 4, 3, 2, 1, 1]

# Example 5.2: sorted() - Returns a new sorted list (original list unchanged)
original_list = [3, 1, 4, 1, 5]
new_sorted_list = sorted(original_list)
print(f"Original list: {original_list}") # Output: Original list: [3, 1, 4, 1, 5]
print(f"New sorted list: {new_sorted_list}") # Output: New sorted list: [1, 1, 3, 4, 5]

# Corner Case: Sorting lists with mixed types (TypeError)
mixed_sort_list = [1, 'b', 3, 'a']
try:
    mixed_sort_list.sort()
except TypeError as e:
    print(f"Error sorting mixed types: {e}") # Output: Error sorting mixed types: '<' not supported between instances of 'str' and 'int'

# Example 5.3: reverse() - Reverses the list in-place
reverse_list = [1, 2, 3, 4, 5]
reverse_list.reverse()
print(f"After reverse(): {reverse_list}") # Output: [5, 4, 3, 2, 1]

# Example 5.4: reversed() - Returns a new reverse iterator (original list unchanged)
original_reverse_list = [10, 20, 30]
reversed_iterator = reversed(original_reverse_list)
new_reversed_list = list(reversed_iterator) # Convert iterator to list
print(f"Original list: {original_reverse_list}") # Output: Original list: [10, 20, 30]
print(f"New reversed list: {new_reversed_list}") # Output: New reversed list: [30, 20, 10]


# --- 6. Copying Lists ---
# Problem: Create copies of lists without affecting the original.
# Functions/Methods: slicing ([:]), list() constructor, copy.copy() (shallow), copy.deepcopy() (deep)

print("\n--- 6. Copying Lists ---")

list_original = [1, 2, [3, 4]]

# Example 6.1: Shallow copy using slicing ([:])
copy_slice = list_original[:]
copy_slice[0] = 99 # Modifies only copy_slice
copy_slice[2].append(5) # Corner Case: Modifies the nested list in BOTH original and copy_slice
print(f"Original after slice copy mod: {list_original}") # Output: Original after slice copy mod: [1, 2, [3, 4, 5]]
print(f"Slice copy: {copy_slice}") # Output: Slice copy: [99, 2, [3, 4, 5]]

# Example 6.2: Shallow copy using list() constructor
copy_constructor = list(list_original)
copy_constructor[0] = 100
copy_constructor[2].append(6) # Corner Case: Modifies the nested list in BOTH original and copy_constructor
print(f"Original after constructor copy mod: {list_original}") # Output: Original after constructor copy mod: [1, 2, [3, 4, 5, 6]]
print(f"Constructor copy: {copy_constructor}") # Output: Constructor copy: [100, 2, [3, 4, 5, 6]]

# Example 6.3: Deep copy using copy.deepcopy()
# This creates a completely independent copy, including nested mutable objects.
deep_copy = copy.deepcopy(list_original)
deep_copy[0] = 200
deep_copy[2].append(7) # Modifies only deep_copy's nested list
print(f"Original after deep copy mod: {list_original}") # Output: Original after deep copy mod: [1, 2, [3, 4, 5, 6]]
print(f"Deep copy: {deep_copy}") # Output: Deep copy: [200, 2, [3, 4, 5, 6, 7]]


# --- 7. List Comprehension ---
# Problem: Create new lists concisely based on existing iterables, with filtering and transformation.
# Functions/Methods: [expression for item in iterable if condition]

print("\n--- 7. List Comprehension ---")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Example 7.1: Filtering even numbers
even_numbers = [n for n in numbers if n % 2 == 0]
print(f"Even numbers: {even_numbers}") # Output: [2, 4, 6, 8, 10]

# Example 7.2: Transforming (squaring) numbers
squared_numbers = [n**2 for n in numbers]
print(f"Squared numbers: {squared_numbers}") # Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Example 7.3: Filtering and transforming
even_squares = [n**2 for n in numbers if n % 2 == 0]
print(f"Even squares: {even_squares}") # Output: [4, 16, 36, 64, 100]

# Example 7.4: Nested list comprehension (flattening a list of lists)
nested = [[1, 2], [3, 4], [5, 6]]
flattened = [item for sublist in nested for item in sublist]
print(f"Flattened list: {flattened}") # Output: [1, 2, 3, 4, 5, 6]

# Example 7.5: Conditional expression within list comprehension
fizzbuzz_list = ["FizzBuzz" if i % 15 == 0 else "Fizz" if i % 3 == 0 else "Buzz" if i % 5 == 0 else i for i in range(1, 16)]
print(f"FizzBuzz list: {fizzbuzz_list}")
# Output: FizzBuzz list: [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz']


# --- 8. Common List Use Cases ---

print("\n--- 8. Common List Use Cases ---")

# Example 8.1: Implementing a Stack (LIFO - Last In, First Out)
# Functions/Methods: append() for push, pop() for pop
stack = []
stack.append('A') # Push
stack.append('B') # Push
print(f"Stack after pushes: {stack}") # Output: ['A', 'B']
popped_item = stack.pop() # Pop
print(f"Popped item: {popped_item}") # Output: B
print(f"Stack after pop: {stack}") # Output: ['A']

# Example 8.2: Implementing a Queue (FIFO - First In, First Out)
# Functions/Methods: append() for enqueue, pop(0) for dequeue (less efficient for large lists)
# For efficient queues, use collections.deque
queue = []
queue.append('X') # Enqueue
queue.append('Y') # Enqueue
print(f"Queue after enqueues: {queue}") # Output: ['X', 'Y']
dequeued_item = queue.pop(0) # Dequeue
print(f"Dequeued item: {dequeued_item}") # Output: X
print(f"Queue after dequeue: {queue}") # Output: ['Y']

# Better for Queue: collections.deque
from collections import deque
efficient_queue = deque()
efficient_queue.append('P')
efficient_queue.append('Q')
print(f"Efficient Queue: {efficient_queue}") # Output: deque(['P', 'Q'])
print(f"Dequeued from efficient queue: {efficient_queue.popleft()}") # Output: P

# Example 8.3: Iterating with index (enumerate)
data = ['item1', 'item2', 'item3']
for index, value in enumerate(data):
    print(f"Index {index}: {value}")
# Output:
# Index 0: item1
# Index 1: item2
# Index 2: item3

# Example 8.4: Data Aggregation
sales_data = [
    {'product': 'A', 'revenue': 100},
    {'product': 'B', 'revenue': 150},
    {'product': 'A', 'revenue': 50},
]
total_revenue = sum(item['revenue'] for item in sales_data)
print(f"Total revenue: {total_revenue}") # Output: Total revenue: 300

product_revenue = collections.defaultdict(float)
for sale in sales_data:
    product_revenue[sale['product']] += sale['revenue']
print(f"Revenue by product: {dict(product_revenue)}") # Output: Revenue by product: {'A': 150.0, 'B': 150.0}


# --- 9. Checking for Subsets/Supersets of Elements ---
# Problem: Determine if all or any elements from one list are present in another.
# Functions/Methods: all(), any(), set() for efficiency

print("\n--- 9. Checking for Subsets/Supersets of Elements ---")

main_set_of_items = ['apple', 'banana', 'cherry', 'date', 'elderberry']
required_items = ['apple', 'cherry']
optional_items = ['grape', 'banana']
missing_items = ['kiwi', 'mango']

# Example 9.1: Check if ALL required items are present (subset check)
# Convert to sets for efficient intersection/subset checks
all_present = all(item in main_set_of_items for item in required_items)
print(f"Are all required items present? {all_present}") # Output: True

# More efficient with sets:
all_present_set = set(required_items).issubset(set(main_set_of_items))
print(f"Are all required items present (set)? {all_present_set}") # Output: True

# Example 9.2: Check if ANY optional items are present
any_present = any(item in main_set_of_items for item in optional_items)
print(f"Are any optional items present? {any_present}") # Output: True

# More efficient with sets:
any_present_set = not set(optional_items).isdisjoint(set(main_set_of_items))
print(f"Are any optional items present (set)? {any_present_set}") # Output: True

# Example 9.3: Check if NO items are present
none_present = not any(item in main_set_of_items for item in missing_items)
print(f"Are none of the missing items present? {none_present}") # Output: True

# More efficient with sets:
none_present_set = set(missing_items).isdisjoint(set(main_set_of_items))
print(f"Are none of the missing items present (set)? {none_present_set}") # Output: True


# --- 10. Finding Min/Max with Custom Key ---
# Problem: Find the minimum or maximum element in a list based on a specific attribute or calculation.
# Functions/Methods: min(), max() with 'key' argument

print("\n--- 10. Finding Min/Max with Custom Key ---")

products = [
    {'name': 'Laptop', 'price': 1200, 'weight': 2.5},
    {'name': 'Mouse', 'price': 25, 'weight': 0.1},
    {'name': 'Keyboard', 'price': 75, 'weight': 0.8},
    {'name': 'Monitor', 'price': 300, 'weight': 5.0}
]

# Example 10.1: Find the cheapest product
cheapest_product = min(products, key=lambda p: p['price'])
print(f"Cheapest product: {cheapest_product['name']} (${cheapest_product['price']})") # Output: Mouse ($25)

# Example 10.2: Find the heaviest product
heaviest_product = max(products, key=lambda p: p['weight'])
print(f"Heaviest product: {heaviest_product['name']} ({heaviest_product['weight']}kg)") # Output: Monitor (5.0kg)

# Corner Case: Empty list (raises ValueError)
empty_products = []
try:
    min(empty_products, key=lambda p: p['price'])
except ValueError as e:
    print(f"Error finding min in empty list: {e}") # Output: Error finding min in empty list: min() arg is an empty sequence


# --- 11. Joining List Elements into a String ---
# Problem: Concatenate elements of a list into a single string, with a specified separator.
# Functions/Methods: str.join()

print("\n--- 11. Joining List Elements into a String ---")

words = ['Hello', 'World', 'Python']
numbers_as_strings = ['1', '2', '3']
mixed_list = ['apple', 123, 'banana'] # Will cause error if not all strings

# Example 11.1: Join with space
sentence = " ".join(words)
print(f"Joined with space: '{sentence}'") # Output: 'Hello World Python'

# Example 11.2: Join with comma and space
csv_string = ", ".join(words)
print(f"Joined with comma and space: '{csv_string}'") # Output: 'Hello, World, Python'

# Example 11.3: Join numbers (after converting to string)
num_string = "-".join(str(n) for n in numbers_as_strings)
print(f"Joined numbers: '{num_string}'") # Output: '1-2-3'

# Corner Case: Non-string elements (raises TypeError)
try:
    " ".join(mixed_list)
except TypeError as e:
    print(f"Error joining mixed types: {e}") # Output: Error joining mixed types: sequence item 1: expected str instance, int found

# Solution for mixed types: Convert all to string first
mixed_joined = " ".join(str(item) for item in mixed_list)
print(f"Joined mixed types (converted): '{mixed_joined}'") # Output: 'apple 123 banana'


# --- 12. Removing Duplicates (Maintaining Order) ---
# Problem: Get unique elements from a list while preserving their original order.
# Functions/Methods: Using collections.OrderedDict (Python 3.7+), dict.fromkeys(), or a loop with a set

print("\n--- 12. Removing Duplicates (Maintaining Order) ---")

data_with_duplicates = [1, 5, 2, 8, 5, 1, 9, 2]

# Example 12.1: Using dict.fromkeys() (most concise for Python 3.7+)
# dict.fromkeys creates keys from iterable, and since keys must be unique, duplicates are ignored.
# In Python 3.7+, dicts preserve insertion order.
unique_ordered_from_dict = list(dict.fromkeys(data_with_duplicates))
print(f"Unique (ordered, dict.fromkeys): {unique_ordered_from_dict}") # Output: [1, 5, 2, 8, 9]

# Example 12.2: Using a loop with a set (more explicit)
seen = set()
unique_ordered_loop = []
for item in data_with_duplicates:
    if item not in seen:
        unique_ordered_loop.append(item)
        seen.add(item)
print(f"Unique (ordered, loop+set): {unique_ordered_loop}") # Output: [1, 5, 2, 8, 9]

# Corner Case: Elements must be hashable for set/dict.fromkeys()
unhashable_list = [[1], [2], [1]]
try:
    list(dict.fromkeys(unhashable_list))
except TypeError as e:
    print(f"Error removing duplicates with unhashable items: {e}") # Output: Error removing duplicates with unhashable items: unhashable type: 'list'


# --- 13. Flattening Nested Lists (More Complex) ---
# Problem: Convert a list of lists (or deeply nested lists) into a single flat list.
# Functions/Methods: Nested list comprehensions, recursion, itertools.chain()

print("\n--- 13. Flattening Nested Lists (More Complex) ---")

list_of_lists = [[1, 2], [3, 4, 5], [6]]
deeply_nested = [1, [2, 3], [4, [5, 6]], 7]

# Example 13.1: Flattening a 2D list (nested list comprehension)
flat_2d = [item for sublist in list_of_lists for item in sublist]
print(f"Flattened 2D list: {flat_2d}") # Output: [1, 2, 3, 4, 5, 6]

# Example 13.2: Flattening arbitrarily nested lists (recursive function)
def flatten_recursive(nested_list):
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten_recursive(item))
        else:
            flat_list.append(item)
    return flat_list

flat_deeply_nested = flatten_recursive(deeply_nested)
print(f"Flattened deeply nested (recursive): {flat_deeply_nested}") # Output: [1, 2, 3, 4, 5, 6, 7]

# Example 13.3: Flattening with itertools.chain (for 1 level of nesting)
# itertools.chain is very efficient for concatenating iterables
flat_chain = list(itertools.chain.from_iterable(list_of_lists))
print(f"Flattened with itertools.chain: {flat_chain}") # Output: [1, 2, 3, 4, 5, 6]

# Corner Case: itertools.chain.from_iterable expects an iterable of iterables.
# If you pass a list of non-iterables, it will raise a TypeError.
try:
    list(itertools.chain.from_iterable([1, 2, 3])) # 1, 2, 3 are not iterables
except TypeError as e:
    print(f"Error with itertools.chain on non-iterables: {e}") # Output: Error with itertools.chain on non-iterables: 'int' object is not iterable


# --- 14. Transforming Lists with map() and filter() ---
# Problem: Apply a function to each item or filter items based on a condition, functionally.
# Functions/Methods: map(), filter(), lambda functions

print("\n--- 14. Transforming Lists with map() and filter() ---")

data_numbers = [1, 2, 3, 4, 5]
data_words = ['apple', 'banana', 'cherry']

# Example 14.1: Squaring numbers using map()
squared_map = list(map(lambda x: x**2, data_numbers))
print(f"Squared numbers (map): {squared_map}") # Output: [1, 4, 9, 16, 25]

# Example 14.2: Filtering even numbers using filter()
even_filter = list(filter(lambda x: x % 2 == 0, data_numbers))
print(f"Even numbers (filter): {even_filter}") # Output: [2, 4]

# Example 14.3: Combining map and filter
# Get lengths of words longer than 5 characters
long_word_lengths = list(map(len, filter(lambda w: len(w) > 5, data_words)))
print(f"Lengths of long words: {long_word_lengths}") # Output: [6]

# Corner Case: map/filter return iterators, need to convert to list/tuple for display
# If you don't convert, they will only be consumed once.
map_iterator = map(lambda x: x * 2, [1, 2, 3])
print(f"Map iterator (first pass): {list(map_iterator)}") # Output: [2, 4, 6]
print(f"Map iterator (second pass, empty): {list(map_iterator)}") # Output: []


# --- 15. Finding Intersections, Differences, and Unions between Lists ---
# Problem: Compare elements across multiple lists.
# Functions/Methods: Convert to set for efficient set operations (&, |, -, ^)

print("\n--- 15. Finding Intersections, Differences, and Unions between Lists ---")

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
list3 = [3, 7, 9]

set1 = set(list1)
set2 = set(list2)
set3 = set(list3)

# Example 15.1: Intersection (elements common to both)
intersection = list(set1 & set2)
print(f"Intersection of list1 and list2: {intersection}") # Output: [4, 5] (order not guaranteed)

# Example 15.2: Union (all unique elements from both)
union = list(set1 | set2)
print(f"Union of list1 and list2: {union}") # Output: [1, 2, 3, 4, 5, 6, 7, 8] (order not guaranteed)

# Example 15.3: Difference (elements in list1 but not list2)
difference = list(set1 - set2)
print(f"Elements in list1 but not list2: {difference}") # Output: [1, 2, 3] (order not guaranteed)

# Example 15.4: Symmetric Difference (elements unique to either list1 or list2)
symmetric_difference = list(set1 ^ set2)
print(f"Elements unique to list1 or list2: {symmetric_difference}") # Output: [1, 2, 3, 6, 7, 8] (order not guaranteed)

# Example 15.5: Intersection of multiple lists
multi_intersection = list(set1 & set2 & set3)
print(f"Intersection of list1, list2, list3: {multi_intersection}") # Output: [7, 3] (order not guaranteed)

# Corner Case: Handling unhashable items in lists before converting to set
# If your lists contain mutable objects (like other lists), you cannot directly convert them to sets.
unhashable_elements_list = [1, [2, 3], 4]
try:
    set(unhashable_elements_list)
except TypeError as e:
    print(f"Error converting list with unhashable elements to set: {e}") # Output: Error converting list with unhashable elements to set: unhashable type: 'list'

