def reverse_number(n):
    return int(str(n)[::-1])

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def find_palindrome(n):
    while True:
        reversed_n = reverse_number(n)
        n = n + reversed_n
        if is_palindrome(n):
            return n

original_number = int(input("enter the number : "))
palindrome_sum = find_palindrome(original_number)
print(f"The palindrome sum is: {palindrome_sum}")
