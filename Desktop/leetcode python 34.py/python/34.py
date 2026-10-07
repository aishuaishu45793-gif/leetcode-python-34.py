# 104 Move zeros to the end

numbers = [0, 1, 0, 3, 12, 0, 5]

result = []

for number in numbers:
    if number != 0:
        result.append(number)

zero_count = len(numbers) - len(result)

result += [0] * zero_count

print("Result:", result)