def fibonacci_series(n):
    series = []
    a, b = 0, 1  # First two numbers in the series
    
    for _ in range(n):
        series.append(b)  # Append the current number
        a, b = b, a + b   # Update values of a and b
    
    return series

n_terms = int(input("Enter the number of terms: "))

if n_terms <= 0:
    print("Please enter a positive integer.")

else:
    print("Fibonacci series:")
    print(fibonacci_series(n_terms))