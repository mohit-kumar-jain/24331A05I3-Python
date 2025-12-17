import itertools
import functools
import operator
import statistics

numbers = [2, 4, 6, 8]
cumulative_sum = list(itertools.accumulate(numbers))

product_of_numbers = functools.reduce(operator.mul, numbers)

average_value = statistics.fmean(numbers)

quotient, remainder = divmod(29, 5)

indexed_data = list(enumerate(numbers, start=10))

all_even = all(n % 2 == 0 for n in numbers)
any_greater_than_five = any(n > 5 for n in numbers)

print("Numbers:", numbers)
print("Cumulative sum:", cumulative_sum)
print("Product of numbers:", product_of_numbers)
print("Average (fmean):", average_value)
print("Divmod result → Quotient:", quotient, "Remainder:", remainder)
print("Enumerate starting at 10:", indexed_data)
print("Are all numbers even?", all_even)
print("Is any number > 5?", any_greater_than_five)