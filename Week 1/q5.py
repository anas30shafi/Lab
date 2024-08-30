def calculate_cubes(n):
    cubes = {i: i**3 for i in range(1, n+1)}
    return cubes


n = int(input("Enter a number: "))
cubes = calculate_cubes(n)
print(f"The cubes of numbers from 1 to {n} are: {cubes}")
