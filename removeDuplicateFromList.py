numberList = [1, 2, 400, 2, 19, 20, 1, 200]
print(numberList)
noDuplicateNumberList = []
for number in numberList:
    # duplicate =
    if number not in noDuplicateNumberList:
        noDuplicateNumberList.append(number)
print(noDuplicateNumberList)