# Memoization optimizes recursion by storing previous results. 
# Here’s the Fibonacci sequence computed with a dynamic programming approach.

def fibonacci_memo(n, memo={}):  # type: ignore
    """Compute the nth Fibonacci number using memoization"""
    if n in memo:
        return memo[n]  # type: ignore
    if n <= 1:
        return n # type: ignore
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo) # type: ignore
    return memo[n] # type: ignore

print("Fibonacci numbers (memoized):")
for i in range(10):
    print(f"Fibonacci({i}) = {fibonacci_memo(i)}")