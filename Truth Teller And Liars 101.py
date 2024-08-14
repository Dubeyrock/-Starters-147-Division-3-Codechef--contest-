def find_minimum_queries(T, test_cases):
    """
    This function determines the minimum number of queries required to ensure
    the correct path to eternal happiness based on the number of truth tellers
    (N) and liars (M). 

    Approach:
    - If the number of liars (M) is greater than or equal to the number of truth tellers (N),
      it's impossible to determine the correct path since the liars can outvote the truth tellers.
      In this case, we append -1 to the results.
    - Otherwise, to ensure that we have a majority of truth tellers responding, we need to ask
      at least (2 * M + 1) people. This guarantees that even in the worst-case scenario, the
      truth tellers will dominate the responses, allowing us to determine the correct path.

    Implementation:
    - Iterate through each test case.
    - For each (N, M), check if M >= N; if so, append -1 to results.
    - If not, calculate the minimum number of queries as (2 * M + 1) and append to results.
    
    Pseudocode:
    1. Function find_minimum_queries(T, test_cases):
    2. Initialize results list
    3. For each (N, M) in test_cases:
    4.     If M >= N:
    5.         Append -1 to results
    6.     Else:
    7.         Calculate X = 2 * M + 1
    8.         Append X to results
    9. Return results

    Time Complexity:
    - The time complexity is O(T), where T is the number of test cases. Each test case
      is processed in constant time, O(1), resulting in an overall linear complexity.

    Summary of the Code:
    - The code reads the number of test cases and the values of N and M for each test case.
    - It checks the conditions for determining the path to happiness based on the number of truth tellers and liars.
    - Finally, it outputs the minimum number of queries needed for each test case or -1 if it is impossible.
    """

    results = []
    for N, M in test_cases:
        if M >= N:
            results.append(-1)  # Impossible to determine the path
        else:
            X = 2 * M + 1  # Minimum queries needed to ensure majority
            results.append(X)
    return results

# Read input and execute the function
T = int(input())
test_cases = [tuple(map(int, input().split())) for _ in range(T)]
results = find_minimum_queries(T, test_cases)
for result in results:
    print(result)
