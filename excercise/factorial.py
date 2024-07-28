def factorial(n, cache={}):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    
    if n in cache:
        return cache[n]
    
    if n == 0 or n == 1:
        cache[n] = 1
    else:
        cache[n] = n * factorial(n - 1, cache)
    
    return cache[n]

# Example usage
num = int(input("enter the number"))
print(f"The factorial of {num} is: {factorial(num)}")

# Printing the cache to show stored factorials
print("Factorials cache:", factorial(num, cache={}))
