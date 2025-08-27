def fibonacci_recursive(n): # type: ignore
    # sourcery skip: assign-if-exp, reintroduce-else
    """"Calculate the nth Fibonacci number using recursion."""
    if n <= 1:
        return n # type: ignore
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2) # type: ignore

print("Fibonacci numbers (recursive):")
for i in range(10):
    print(f"Fibonacci({i}) = {fibonacci_recursive(i)}")