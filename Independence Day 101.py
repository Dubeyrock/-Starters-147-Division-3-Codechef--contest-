def can_design_flag(a, b, c):
    """
    This function determines if it is possible to design a flag using all strips
    of three colors such that no two adjacent strips share the same color.

    Approach:
    - To ensure no two adjacent strips share the same color, we can derive a condition based on the maximum number
      of strips available in any single color.
    - If the maximum number of strips of any color (let's say `max_strips`) is more than the sum of the other two colors
      plus one, it is impossible to arrange the strips without having adjacent strips of the same color.
    - Thus, we need to check the condition: `max_strips <= (total_strips - max_strips + 1)`

    Implementation:
    - Read the number of test cases.
    - For each test case, read the counts of orange, white, and green strips.
    - Calculate the maximum of the three counts and check the above condition.
    - Print "YES" if the arrangement is possible, otherwise print "NO".

    Pseudocode:
    function can_design_flag(a, b, c):
        max_strips = max(a, b, c)
        total_strips = a + b + c
        if max_strips <= (total_strips - max_strips + 1):
            return YES
        else:
            return NO

    main:
        read T
        for i from 1 to T:
            read a, b, c
            print can_design_flag(a, b, c)

    Time Complexity:
    - O(1) for each test case as the operations performed are constant time.
    - Total time complexity is O(T), where T is the number of test cases.

    Summary of Code:
    - The code reads the number of test cases and, for each case, determines if it is possible to arrange the
      strips without adjacent colors being the same. It utilizes a simple mathematical condition to check this,
      ensuring efficiency even with the upper constraint limits.
    """

    # Calculate the maximum number of strips and total strips
    max_strips = max(a, b, c)
    total_strips = a + b + c

    # Check if the arrangement is possible
    return max_strips <= (total_strips - max_strips + 1)

def main():
    t = int(input())  # Read number of test cases
    for _ in range(t):
        a, b, c = map(int, input().split())  # Read three integers (A, B, C)
        if can_design_flag(a, b, c):
            print("YES")  # Arrangement is possible
        else:
            print("NO")   # Arrangement is not possible

if __name__ == "__main__":
    main()

