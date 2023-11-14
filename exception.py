try:
    age = int(input("Enter age"))
    incomePerYear = 20000 / age
    print(incomePerYear)
except ZeroDivisionError:
    print("Age can't be 0.")