def fibonacci_iterative(n):
    if n <= 0:
        return 0
    elif n == 2: #Fix me
        return 1
    
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a + b
 return b # Fix me.

n = 10
print(f"The {n}th Fibonacci number is: {fibonacci_iterative(n)}")