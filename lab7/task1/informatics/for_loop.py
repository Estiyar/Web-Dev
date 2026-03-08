##
def problem_a():
    """Read N; print integers from 1 to N, one per line."""
    n = int(input())
    for i in range(1, n + 1):
        print(i)



def problem_b():
    """Read N; print the sum 1 + 2 + ... + N."""
    n = int(input())
    total = 0
    for i in range(1, n + 1):
        total += i
    print(total)



def problem_c():
    """
    Read N, then N integers on separate lines.
    Print their sum.
    """
    n = int(input())
    total = 0
    for _ in range(n):
        total += int(input())
    print(total)



def problem_d():
    """Read N; print N! (factorial)."""
    n = int(input())
    result = 1
    for i in range(2, n + 1):
        result *= i
    print(result)



def problem_e():
    """Read N; count and print how many even numbers are in [1, N]."""
    n = int(input())
    count = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            count += 1
    print(count)



def problem_f():
    """Read N, then N integers. Print the minimum."""
    n = int(input())
    numbers = [int(input()) for _ in range(n)]
    print(min(numbers))



def problem_g():
    """Read N, then N integers. Print the maximum."""
    n = int(input())
    numbers = [int(input()) for _ in range(n)]
    print(max(numbers))



def problem_h():
    """
    Read N. Print the multiplication table row for N (from 1*N to 10*N).
    """
    n = int(input())
    for i in range(1, 11):
        print(f"{n} * {i} = {n * i}")



def problem_i():
    """Read N; print N asterisks on one line separated by spaces."""
    n = int(input())
    print(" ".join("*" * n))



def problem_j():
    """Read a positive integer; print the sum of its digits."""
    n = input().strip()
    print(sum(int(d) for d in n))



def problem_k():
    """Read N; print the count of its divisors."""
    n = int(input())
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    print(count)



def problem_l():
    """Read N; print integers from N down to 1, one per line."""
    n = int(input())
    for i in range(n, 0, -1):
        print(i)



def problem_m():
    """
    Read base a and exponent b.
    Print a^b without using ** or pow().
    """
    a, b = map(int, input().split())
    result = 1
    for _ in range(b):
        result *= a
    print(result)


