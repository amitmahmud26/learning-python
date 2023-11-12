numbers = [1, 4, 6, 9, 3, 9983, 84393, -94993939, 0, 3]
largest = numbers[0]
for number in numbers:
    if largest < number:
        largest = number
print(largest)