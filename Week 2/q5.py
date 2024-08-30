def sum_of_digits(num):
    return sum(int(digit) for digit in str(num))

user_number = int(input("Enter an integer: "))
digit_sum = sum_of_digits(user_number)
print(f"Sum of digits: {digit_sum}")
