"""
Given an array of positive integers a, your task is to calculate the sum of every possible a[i] ∘ a[j], where a[i] ∘ a[j] is the concatenation of the string representations of a[i] and a[j] respectively.
"""
import collections
def concatenationsSum(a):
    total = 0
    
    length_to_count = collections.defaultdict(int)
    for num in a:
        length_to_count[len(str(num))] += 1
    for i in range(len(a)):
        for length, count in length_to_count.items():
            total += a[i] * (count * pow(10, length))
        total += len(a) * a[i]
    return total

