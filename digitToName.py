# phoneNo = input("Phone: ")
# for i in phoneNo:
#     if int(i) == 1:
#         print("One")
#     elif int(i) == 2:
#         print("Two")
#     elif int(i) == 3:
#         print("Three")
#     elif int(i) == 4:
#         print("Four")
#     elif int(i) == 5:
#         print("Five")
#     elif int(i) == 6:
#         print("Six")
#     elif int(i) == 7:
#         print("Seven")
#     elif int(i) == 8:
#         print("Eight")
#     elif int(i) == 9:
#         print("Nine")
#     else:
#         print("Zero")

phone = input("Phone: ")
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}
output = ""
for ch in phone:
    output += (digits_mapping.get(ch)) + " "
print(output)
