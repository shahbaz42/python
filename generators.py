# Define a generator function that generates a sequence of Fibonacci numbers
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Create a generator object using the fibonacci() generator function
fib_generator = fibonacci()

# Print the first 10 Fibonacci numbers using a for loop
print("First 10 Fibonacci numbers:")
for i in range(10):
    print(next(fib_generator))

# Define a generator function that generates a sequence of squares of numbers
def squares(n):
    for i in range(n):
        yield i**2

# Create a generator object using the squares() generator function
squares_generator = squares(5)

# Print the squares of numbers from 0 to 4 using the generator
print("\nSquares of numbers:")
print(next(squares_generator))  # Output: 0
print(next(squares_generator))  # Output: 1
print(next(squares_generator))  # Output: 4
print(next(squares_generator))  # Output: 9
print(next(squares_generator))  # Output: 16

# Use a generator expression to generate even numbers
even_generator = (x for x in range(10) if x % 2 == 0)

# Print the even numbers using a while loop and next()
print("\nEven numbers:")
while True:
    try:
        print(next(even_generator))
    except StopIteration:
        break
