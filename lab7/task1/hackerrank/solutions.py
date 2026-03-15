

print("Hello, World!")




def py_if_else():
    n = int(input())
    if n % 2 != 0:
        print("Weird")
    elif n % 2 == 0 and 2 <= n <= 5:
        print("Not Weird")
    elif n % 2 == 0 and 6 <= n <= 20:
        print("Weird")
    else:
        print("Not Weird")



def arithmetic_operators():
    a = int(input())
    b = int(input())
    print(a + b)
    print(a - b)
    print(a * b)




def python_division():
    a = int(input())
    b = int(input())
    print(a // b)   # integer division
    print(a / b)    # float division



def loops_challenge():
    n = int(input())
    for i in range(n):
        print(i * i)




def print_function():
    n = int(input())
    print(*range(1, n + 1), sep="")




def runner_up_score():
    _ = int(input())
    arr = list(map(int, input().split()))
    arr = list(set(arr))
    arr.sort()
    print(arr[-2])




def split_and_join(line):
    return "-".join(line.split())




def sets_average():
    _ = input()
    arr = list(map(int, input().split()))
    unique = set(arr)
    print(sum(unique) / len(unique))



def dict_problem():
    """
    Given a dictionary of name: marks pairs,
    print each name and mark sorted by name.
    """
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores

    query = input()
    marks = student_marks[query]
    print(round(sum(marks) / len(marks), 2))



