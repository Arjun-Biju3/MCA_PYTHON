from armstrong import generate_armstrong_numbers

start_limit = int(input("Enter the start limit: "))
end_limit = int(input("Enter the end limit: "))

armstrong_numbers = generate_armstrong_numbers(start_limit, end_limit)
print("Armstrong numbers between", start_limit," and", end_limit,":", armstrong_numbers)
