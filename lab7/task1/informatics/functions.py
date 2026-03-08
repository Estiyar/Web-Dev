##
def maximum(a, b):
    """Return the larger of two numbers."""
    return a if a >= b else b


def problem_a():
    a, b = map(int, input().split())
    print(maximum(a, b))



def is_prime(n):
    """Return True if n is a prime number, False otherwise."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def problem_b():
    """Read N integers; print "YES" if prime, "NO" otherwise for each."""
    n = int(input())
    for _ in range(n):
        num = int(input())
        print("YES" if is_prime(num) else "NO")



def fibonacci(n):
    """Return the n-th Fibonacci number (0-indexed: fib(0)=0, fib(1)=1)."""
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def problem_c():
    """Read N; print the N-th Fibonacci number."""
    n = int(input())
    print(fibonacci(n))


