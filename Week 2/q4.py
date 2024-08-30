def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

user_number = int(input("Enter a number: "))
print(f"Factorial of {user_number} = {factorial(user_number)}")
