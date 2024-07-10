string1 = input().split(", ")
numbers = [int(word) for word in string1]
positive1 = [num for num in numbers if num >= 0]
negative1 = [num for num in numbers if num < 0]
even1 = [num for num in numbers if num % 2 == 0]
odd1 = [num for num in numbers if num % 2 != 0]
print(f"Positive: {', '.join(map(str, positive1))}")
print(f"Negative: {', '.join(map(str, negative1))}")
print(f"Even: {', '.join(map(str, even1))}")
print(f"Odd: {', '.join(map(str, odd1))}")