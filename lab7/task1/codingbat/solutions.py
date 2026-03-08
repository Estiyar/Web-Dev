##

def sleep_in(weekday, vacation):
    """Return True if we can sleep in — not a weekday or on vacation."""
    return not weekday or vacation


def monkey_trouble(a_smile, b_smile):
    """Return True if both or neither monkey is smiling."""
    return a_smile == b_smile


def sum_double(a, b):
    """Return a+b; if they're equal, return double."""
    total = a + b
    return total * 2 if a == b else total


def diff21(n):
    """Return absolute difference from 21; double if n > 21."""
    diff = abs(21 - n)
    return diff * 2 if n > 21 else diff


def parrot_trouble(talking, hour):
    """True if parrot is talking and it's before 7 or after 20."""
    return talking and (hour < 7 or hour > 20)


def makes10(a, b):
    """True if one of the values is 10, or they sum to 10."""
    return a == 10 or b == 10 or a + b == 10


def near_hundred(n):
    """True if n is within 10 of 100 or 200."""
    return abs(100 - n) <= 10 or abs(200 - n) <= 10


def pos_neg(a, b, negative):
    """True if one is negative, the other positive; or both negative if flag."""
    if negative:
        return a < 0 and b < 0
    return (a < 0) != (b < 0)


def not_string(str):
    """Add 'not ' to the front of str; if str already begins with 'not', leave unchanged."""
    if str.startswith("not"):
        return str
    return "not " + str


def missing_char(str, n):
    """Return str with the char at index n removed."""
    return str[:n] + str[n + 1:]


def front_back(str):
    """Swap the first and last chars of str."""
    if len(str) <= 1:
        return str
    return str[-1] + str[1:-1] + str[0]


def front3(str):
    """Return a string made of the first 3 chars, repeated 3 times."""
    front = str[:3]
    return front * 3




def string_times(str, n):
    """Return str repeated n times."""
    return str * n


def front_times(str, n):
    """Return first 3 chars of str, repeated n times."""
    return str[:3] * n


def string_bits(str):
    """Return every other char from str, starting with index 0."""
    return str[::2]


def string_splosion(str):
    """
    Return a string where for every char in str,
    we have all the chars from str up to and including that char.
    Example: "Code" → "CCoCodCode"
    """
    result = ""
    for i in range(len(str)):
        result += str[:i + 1]
    return result


def last2(str):
    """Count how many times the last 2 chars appear in str (non-overlapping, excluding the final occurrence)."""
    if len(str) < 2:
        return 0
    last = str[-2:]
    count = 0
    for i in range(len(str) - 2):
        if str[i:i + 2] == last:
            count += 1
    return count


def array_count9(nums):
    """Return the count of 9s in the list."""
    return nums.count(9)


def array_front9(nums):
    """True if one of the first 4 elements in nums is 9."""
    return 9 in nums[:4]


def array123(nums):
    """True if nums contains 1, 2, 3 consecutively."""
    for i in range(len(nums) - 2):
        if nums[i] == 1 and nums[i + 1] == 2 and nums[i + 2] == 3:
            return True
    return False


def string_match(a, b):
    """Count positions where a 2-char match exists at the same index in both strings."""
    count = 0
    for i in range(min(len(a), len(b)) - 1):
        if a[i:i + 2] == b[i:i + 2]:
            count += 1
    return count



def hello_name(name):
    """Return "Hello Bob!" for name "Bob"."""
    return f"Hello {name}!"


def make_abba(a, b):
    """Return the pattern a+b+b+a."""
    return a + b + b + a


def make_tags(tag, word):
    """Surround word with <tag> and </tag> HTML tags."""
    return f"<{tag}>{word}</{tag}>"


def make_out_word(out, word):
    """
    Given an "out" string of even length, return a new string
    where the word string is in the middle of the out string.
    """
    half = len(out) // 2
    return out[:half] + word + out[half:]


def extra_end(str):
    """Return the last 2 chars of str repeated 3 times."""
    return str[-2:] * 3


def first_two(str):
    """Return the first 2 chars of str, or the whole string if shorter."""
    return str[:2]


def first_half(str):
    """Return the first half of str (even length guaranteed)."""
    return str[:len(str) // 2]


def without_end(str):
    """Return str without the first and last chars."""
    return str[1:-1]


def combo_string(a, b):
    """Return the shorter string + longer string + shorter string."""
    if len(a) <= len(b):
        return a + b + a
    return b + a + b


def non_start(a, b):
    """Return a string made of all but the first char of each string."""
    return a[1:] + b[1:]


def left2(str):
    """Return str with the first 2 chars moved to the end."""
    return str[2:] + str[:2]




def double_char(str):
    """Return a string where every char in str is doubled."""
    return "".join(c * 2 for c in str)


def count_hi(str):
    """Count the number of times 'hi' appears in str."""
    return str.count("hi")


def cat_dog(str):
    """True if str contains same number of 'cat' and 'dog'."""
    return str.count("cat") == str.count("dog")


def count_code(str):
    """Count 'code' occurrences where the 'o' can be any char."""
    count = 0
    for i in range(len(str) - 3):
        if str[i] == "c" and str[i + 2:i + 4] == "de":
            count += 1
    return count


def end_other(a, b):
    """True if either string ends with the other (case-insensitive)."""
    a, b = a.lower(), b.lower()
    return a.endswith(b) or b.endswith(a)


def xyz_there(str):
    """True if str contains 'xyz' not preceded by a period."""
    for i in range(len(str) - 2):
        if str[i:i + 3] == "xyz" and (i == 0 or str[i - 1] != "."):
            return True
    return False




def first_last6(nums):
    """True if 6 appears as first or last element of nums."""
    return len(nums) > 0 and (nums[0] == 6 or nums[-1] == 6)


def same_first_last(nums):
    """True if nums has >= 1 element and first equals last."""
    return len(nums) >= 1 and nums[0] == nums[-1]


def make_pi():
    """Return the first 3 digits of pi: [3, 1, 4]."""
    return [3, 1, 4]


def common_end(a, b):
    """True if both lists have the same first or same last element."""
    return a[0] == b[0] or a[-1] == b[-1]


def sum3(nums):
    """Return the sum of the 3 elements of nums."""
    return sum(nums)


def rotate_left3(nums):
    """Return a list with elements rotated left by one position."""
    return [nums[1], nums[2], nums[0]]


def reverse3(nums):
    """Return a new list with elements in reversed order."""
    return nums[::-1]


def max_end3(nums):
    """Fill a 3-element list with the max of the first/last element."""
    m = max(nums[0], nums[2])
    return [m, m, m]


def sum2(nums):
    """Return the sum of the first 2 elements; if length < 2, use what's available."""
    return sum(nums[:2])


def middle_way(a, b):
    """Return a 2-element list containing the middle elements of a and b."""
    return [a[1], b[1]]


def make_ends(nums):
    """Return a 2-element list with the first and last elements of nums."""
    return [nums[0], nums[-1]]


def has23(nums):
    """True if nums contains 2 or 3."""
    return 2 in nums or 3 in nums




def count_evens(nums):
    """Return the count of even numbers in nums."""
    return sum(1 for n in nums if n % 2 == 0)


def big_diff(nums):
    """Return the difference between the largest and smallest values."""
    return max(nums) - min(nums)


def centered_average(nums):
    """Remove the min and max values; return the integer average of the rest."""
    nums = sorted(nums)
    trimmed = nums[1:-1]
    return sum(trimmed) // len(trimmed)


def sum13(nums):
    """
    Return the sum of nums, but ignore sections starting with a 13 —
    skip the 13 and the number immediately after it.
    """
    total = 0
    skip = False
    for n in nums:
        if skip:
            skip = False
            continue
        if n == 13:
            skip = True
            continue
        total += n
    return total


def sum67(nums):
    """
    Return the sum, but skip any 6..7 sections (from 6 up to and including 7).
    """
    total = 0
    in_section = False
    for n in nums:
        if n == 6:
            in_section = True
        if not in_section:
            total += n
        if n == 7 and in_section:
            in_section = False
    return total


def has22(nums):
    """True if nums contains 2 twice consecutively."""
    for i in range(len(nums) - 1):
        if nums[i] == 2 and nums[i + 1] == 2:
            return True
    return False
