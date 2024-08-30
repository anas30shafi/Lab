def count_digits(num):
    count = 0
    while num != 0:
        num //= 10
        count += 1
    return count

user_number = int(input("Enter an integer: "))
digit_count = count_digits(user_number)
print(f"Total number of digits: {digit_count}")
