def is_palindrome(input_str):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    clean_str = ''.join(input_str.split()).lower()

    # Compare the original string with its reverse
    return clean_str == clean_str[::-1]

# Example usage
user_input = input("Enter a string: ")
if is_palindrome(user_input):
    print(f"{user_input} is a palindrome.")
else:
    print(f"{user_input} is not a palindrome.")
