def is_palindrome(number):
    original_number = number
    reversed_number = 0
    while number > 0:
        reversed_number = reversed_number * 10 + number % 10
        number //= 10
    return original_number == reversed_number
number = int(input("Enter a Number:"))
if is_palindrome(number):
    print("The number is Palindrome")
else:
    print("The number is not a Palindrome")