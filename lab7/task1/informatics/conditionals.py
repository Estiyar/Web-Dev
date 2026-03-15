
def problem_a():
    """
    Read an integer. Print "positive", "negative", or "zero".
    """
    n = int(input())
    if n > 0:
        print("positive")
    elif n < 0:
        print("negative")
    else:
        print("zero")



def problem_b():
    """
    Read two integers. Print the larger one.
    """
    a, b = map(int, input().split())
    if a >= b:
        print(a)
    else:
        print(b)



def problem_c():
    """
    Read three integers. Print the largest.
    """
    a, b, c = map(int, input().split())
    if a >= b and a >= c:
        print(a)
    elif b >= a and b >= c:
        print(b)
    else:
        print(c)



def problem_d():
    """
    Read an integer. Print "even" if divisible by 2, else "odd".
    """
    n = int(input())
    if n % 2 == 0:
        print("even")
    else:
        print("odd")



def problem_e():
    """
    Read a year. Print "YES" if leap year, "NO" otherwise.
    A year is a leap year if divisible by 4, except centuries
    unless also divisible by 400.
    """
    year = int(input())
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("YES")
    else:
        print("NO")



