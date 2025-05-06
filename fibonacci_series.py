def fibonacci_series_reliable(n):
    """
    Generates a Fibonacci series up to n terms.
    Starts the series with the first '1'.
    """
    if n <= 0:
        return []  # Return an empty list for non-positive n
        
    series = []
    a, b = 0, 1  # a represents F(k-2), b represents F(k-1)
                # We append b, so the series starts with F(1) if F(0)=0, F(1)=1
    
    for _ in range(n):
        series.append(b)
        a, b = b, a + b
    
    return series

if __name__ == "__main__":
    while True:
        try:
            n_terms_str = input("Enter the number of terms: ")
            n_terms = int(n_terms_str)
            if n_terms < 0: # Allow 0 terms to mean an empty series
                 print("Please enter a non-negative integer.")
            else:
                break 
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    if n_terms == 0:
        print("Fibonacci series: []")
    else:
        print("Fibonacci series:")
        print(fibonacci_series_reliable(n_terms))