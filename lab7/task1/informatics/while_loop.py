##
def problem_a():
    """
    Read a positive integer N.
    Print the number of digits it has.
    """
    n = int(input())
    count = 0
    if n == 0:
        print(1)
        return
    while n > 0:
        n //= 10
        count += 1
    print(count)



def problem_b():
    """
    Read a positive integer.
    Print its digits in reverse order as an integer.
    Example: 1234 → 4321
    """
    n = int(input())
    reversed_n = 0
    while n > 0:
        digit = n % 10
        reversed_n = reversed_n * 10 + digit
        n //= 10
    print(reversed_n)



def problem_c():
    """
    Read two positive integers.
    Print their Greatest Common Divisor (GCD).
    """
    a, b = map(int, input().split())
    while b != 0:
        a, b = b, a % b
    print(a)



def problem_d():
    """
    Read N. Apply Collatz: if even → N/2, if odd → 3N+1.
    Print the number of steps to reach 1.
    """
    n = int(input())
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        steps += 1
    print(steps)



def problem_e():
    """
    Read integers one by one until 0 is entered.
    Print the sum of all entered numbers (excluding 0).
    """
    total = 0
    while True:
        n = int(input())
        if n == 0:
            break
        total += n
    print(total)


