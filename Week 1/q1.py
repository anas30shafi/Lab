
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))


product_result = num1 * num2
if product_result <= 5000:
    sum_result = num1 + num2
    print(f"Sum of {num1} and {num2} is {sum_result}")
else:
    print(f"Product of {num1} and {num2} is {product_result}")
