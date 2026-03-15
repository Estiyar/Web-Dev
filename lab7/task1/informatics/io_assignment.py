
def problem_a():
    """
    Read two integers from input and print their sum.
    Example: input "3 5" → output "8"
    """
    a, b = map(int, input().split())
    print(a + b)



def problem_b():
    """
    Read two integers, swap them, print both on separate lines.
    Example: input "4 7" → output "7\n4"
    """
    a, b = map(int, input().split())
    a, b = b, a
    print(a)
    print(b)



def problem_c():
    """
    Given width and height of a rectangle, print area then perimeter.
    Example: input "3 4" → output "12\n14"
    """
    width, height = map(int, input().split())
    area = width * height
    perimeter = 2 * (width + height)
    print(area)
    print(perimeter)



def problem_d():
    """
    Read two integers a and b. Print integer division result and remainder.
    Example: input "17 5" → output "3\n2"
    """
    a, b = map(int, input().split())
    print(a // b)
    print(a % b)



def problem_e():
    """
    Read total minutes; print hours and remaining minutes.
    Example: input "135" → output "2\n15"
    """
    total_minutes = int(input())
    hours = total_minutes // 60
    minutes = total_minutes % 60
    print(hours)
    print(minutes)


