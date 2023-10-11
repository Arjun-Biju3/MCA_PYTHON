# Input an integer n
n = int(input("Enter an integer n: "))

# Compute n + nn + nnn
nn = n * 10 + n
nnn = n * 100 + nn
result = n + nn + nnn

# Display the result
print("n + nn + nnn =", result)
