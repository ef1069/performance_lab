# 🔍 Problem 1: Find Most Frequent Element
# Given a list of integers, return the value that appears most frequently.
# If there's a tie, return any of the most frequent.
#
# Example:
# Input: [1, 3, 2, 3, 4, 1, 3]
# Output: 3

def most_frequent(numbers):
    if not numbers:
        return None

    counts = {}
    most_common = numbers[0]
    highest_count = 0

    for number in numbers:
        counts[number] = counts.get(number, 0) + 1

        if counts[number] > highest_count:
            highest_count = counts[number]
            most_common = number

    return most_common

"""
Time and Space Analysis for problem 1:
- Best-case: O(n)
- Worst-case: O(n)
- Average-case: O(n)
- Space complexity: O(n)
- Why this approach? The time and space complexity is mostly affected by the length of the list put through the loop.
A loop is necessary because each number in the list needs to be compared to all the others.
- Could it be optimized? I do not believe this could be optimized, because each number in the list needs to be compared to the others.
"""


# 🔍 Problem 2: Remove Duplicates While Preserving Order
# Write a function that returns a list with duplicates removed but preserves order.
#
# Example:
# Input: [4, 5, 4, 6, 5, 7]
# Output: [4, 5, 6, 7]

def remove_duplicates(nums):
    seen = set()
    result = []

    for num in nums:
        if num not in seen:
            seen.add(num)
            result.append(num)

    return result

"""
Time and Space Analysis for problem 2:
- Best-case: O(n)
- Worst-case: O(n)
- Average-case: O(n)
- Space complexity: O(n)
- Why this approach? Since we want to preserve order and not just print the list as a set, we need to add the unique values
to a new list individually. 
- Could it be optimized? This possibly could be optimized if there was a way to change the list to a set then back to 
a list while preserving order.
"""


# 🔍 Problem 3: Return All Pairs That Sum to Target
# Write a function that returns all unique pairs of numbers in the list that sum to a target.
# Order of output does not matter. Assume input list has no duplicates.
#
# Example:
# Input: ([1, 2, 3, 4], target=5)
# Output: [(1, 4), (2, 3)]

def find_pairs(nums, target):
    meets_target = []
    for num_1 in nums:
        if num_1 <= target:
            for num_2 in nums:
                if num_1 + num_2 == target:
                    meets_target.append((num_1, num_2))
    return meets_target

"""
Time and Space Analysis for problem 3:
- Best-case: O(n^2)
- Worst-case: O(n^2)
- Average-case:O(n^2)
- Space complexity: O(n)
- Why this approach? I created a nested loop so that each element in the list, can be compared to all the others to find if their
sum meets the target.
- Could it be optimized? This could be optimized by findind a way to limit space complexity to add each set as a sum once to limit
space complexity. 
"""


# 🔍 Problem 4: Simulate List Resizing (Amortized Cost)
# Create a function that adds n elements to a list that has a fixed initial capacity.
# When the list reaches capacity, simulate doubling its size by creating a new list
# and copying all values over (simulate this with print statements).
#
# Example:
# add_n_items(6) → should print when resizing happens.

def add_n_items(n):
    add_n_items[1]
    
    pass

"""
Time and Space Analysis for problem 4:
- When do resizes happen?
- What is the worst-case for a single append?
- What is the amortized time per append overall?
- Space complexity:
- Why does doubling reduce the cost overall?
"""


# 🔍 Problem 5: Compute Running Totals
# Write a function that takes a list of numbers and returns a new list
# where each element is the sum of all elements up to that index.
#
# Example:
# Input: [1, 2, 3, 4]
# Output: [1, 3, 6, 10]
# Because: [1, 1+2, 1+2+3, 1+2+3+4]

def running_total(nums):
    # Your code here
    pass

"""
Time and Space Analysis for problem 5:
- Best-case:
- Worst-case:
- Average-case:
- Space complexity:
- Why this approach?
- Could it be optimized?
"""


def main():
    list_1 = [1, 3, 2, 3, 4, 1, 3]
    list_2 = [1, 2, 3, 4]
    print(list_1)
    list_most = most_frequent(list_1)
    print(list_most)
    no_duplicates=remove_duplicates(list_1)
    print(no_duplicates)
    target_list = find_pairs(list_2, 5)
    print(target_list)

main()