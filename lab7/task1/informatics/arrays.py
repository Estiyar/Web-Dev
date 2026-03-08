##
def problem_a():
    """
    Read N, then N integers.
    Print them on one line separated by spaces.
    """
    n = int(input())
    arr = list(map(int, input().split()))
    print(*arr)



def problem_b():
    """
    Read N, then N integers.
    Print the array in reverse order.
    """
    n = int(input())
    arr = list(map(int, input().split()))
    arr.reverse()
    print(*arr)



def problem_c():
    """
    Read N, then N integers.
    Print the second largest unique value.
    """
    n = int(input())
    arr = list(map(int, input().split()))
    unique_sorted = sorted(set(arr), reverse=True)
    print(unique_sorted[1])



def problem_d():
    """
    Read N, the array of N integers, then a target value X.
    Print how many times X appears in the array.
    """
    n = int(input())
    arr = list(map(int, input().split()))
    x = int(input())
    print(arr.count(x))



def problem_e():
    """
    Read N, then N integers.
    Shift all elements one position to the left (first element wraps to end).
    Print the resulting array.
    """
    n = int(input())
    arr = list(map(int, input().split()))
    arr = arr[1:] + [arr[0]]
    print(*arr)



def problem_f():
    """
    Read N, then N integers.
    Print the sum of elements at indices 0, 2, 4, ... (0-based).
    """
    n = int(input())
    arr = list(map(int, input().split()))
    total = sum(arr[i] for i in range(0, n, 2))
    print(total)



def problem_g():
    """
    Read N, then N integers.
    Print the sorted array without duplicate values.
    """
    n = int(input())
    arr = list(map(int, input().split()))
    result = sorted(set(arr))
    print(*result)



