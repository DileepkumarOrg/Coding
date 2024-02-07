def find_digit_position(n, k):
    position = 0
    while n > 0:
        digit = n % 10
        position += 1
        if digit == k:
            return position
        n //= 10

n = int(input("Enter the number (n): "))
k = int(input("Enter the digit (k): "))
position = find_digit_position(n, k)
if position != -1:
    print(f"The digit {k} is present at position {10**(position-1)}s in the number {n}.")
else:
    print(f"The digit {k} is not present in the number {n}.")
