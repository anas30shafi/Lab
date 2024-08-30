def is_palindrome(number):
    return str(number) == str(number)[::-1]


user_number = int(input("Enter a number: "))

if is_palindrome(user_number):
    print(f"{user_number} is a palindrome.")
else:
    print(f"{user_number} is not a palindrome.")
