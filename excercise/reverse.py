def reverse_digits_and_add(num):
    def is_palindrome(n):
        return str(n) == str(n)[::-1]

    def reverse_number(n):
        return int(str(n)[::-1])

    original_number = num
    while True:
        reversed_number = reverse_number(original_number)
        sum_number = original_number + reversed_number
        print(f"{original_number} + {reversed_number} = {sum_number}")

        if is_palindrome(sum_number):
            print(f"Palindrome found: {sum_number}")
            break
        
        original_number = sum_number


num = 123  
reverse_digits_and_add(num)
