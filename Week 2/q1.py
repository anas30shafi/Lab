def extract_digits_reverse(num):
    return [int(digit) for digit in str(num)][::-1]

user_number = int(input("Enter an integer: "))
reversed_digits = extract_digits_reverse(user_number)
print("Digits in reverse order:", reversed_digits)
