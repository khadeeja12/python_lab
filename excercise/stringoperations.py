def check_substring(main_str, sub_str):
    return sub_str in main_str

def count_occurrences(main_str, char):
    return main_str.count(char)

def replace_substring(main_str, old_sub, new_sub):
    return main_str.replace(old_sub, new_sub)

def convert_to_capital(main_str):
    return main_str.upper()

def menu():
    print("String Operations Menu:")
    print("1. Check if the String is a Substring of Another String")
    print("2. Count Occurrences of Character")
    print("3. Replace a Substring with Another Substring")
    print("4. Convert to Capital Letters")
    print("5. Exit")

def main():
    while True:
        menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            main_str = input("Enter the main string: ")
            sub_str = input("Enter the substring to check: ")
            if check_substring(main_str, sub_str):
                print(f"'{sub_str}' is a substring of '{main_str}'.")
            else:
                print(f"'{sub_str}' is not a substring of '{main_str}'.")

        elif choice == '2':
            main_str = input("Enter the main string: ")
            char = input("Enter the character to count: ")
            count = count_occurrences(main_str, char)
            print(f"The character '{char}' occurs {count} times in the string.")

        elif choice == '3':
            main_str = input("Enter the main string: ")
            old_sub = input("Enter the substring to be replaced: ")
            new_sub = input("Enter the new substring: ")
            result = replace_substring(main_str, old_sub, new_sub)
            print(f"Resulting string: {result}")

        elif choice == '4':
            main_str = input("Enter the string to convert to capital letters: ")
            result = convert_to_capital(main_str)
            print(f"String in capital letters: {result}")

        elif choice == '5':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
