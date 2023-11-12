# easy one
# numbers = [5, 2, 5, 2, 2]
# for number in numbers:
#     print("X" * number)

# hard one

numbers = [5, 2, 5, 2, 2]
for number in numbers:
    output = ''
    for n in range(number):
        output += 'X'
    print(output)