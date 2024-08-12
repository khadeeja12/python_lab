def set_union(set1, set2):
    return set1.union(set2)

def set_intersection(set1, set2):
    return set1.intersection(set2)

def set_difference(set1, set2):
    return set1.difference(set2)

def menu():
    print("Set Operations Menu:")
    print("1. Set Union")
    print("2. Set Intersection")
    print("3. Set Difference")
    print("4. Exit")

def fun():
    while True:
        menu()
        choice = input("Enter your choice (1-4): ")

        if choice in ['1', '2', '3']:
            set1 = set(input("Enter the elements of the first set (comma-separated): ").split(','))
            set2 = set(input("Enter the elements of the second set (comma-separated): ").split(','))

            if choice == '1':
                result = set_union(set1, set2)
                print(f"Union of the sets: {result}")
            elif choice == '2':
                result = set_intersection(set1, set2)
                print(f"Intersection of the sets: {result}")
            elif choice == '3':
                result = set_difference(set1, set2)
                print(f"Difference of the sets: {result}")

        elif choice == '4':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

fun()
