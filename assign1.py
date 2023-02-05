# Define a function called "factorial" that takes a single argument "n" and returns the factorial of "n"

def factorial(n):
    fac = 1
    for i in range(1,n+1):
        fac = fac * i
    return fac

print(factorial(5))
