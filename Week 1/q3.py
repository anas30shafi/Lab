user_numbers = [int(input(f"Enter number {i + 1}: ")) for i in range(20)]


divisible_by_5 = [num for num in user_numbers if num % 5 == 0]
print("Numbers divisible by 5:", divisible_by_5)
