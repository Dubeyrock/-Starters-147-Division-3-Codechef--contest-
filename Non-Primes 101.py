def sieve(m_num):
    """
    Sieve of Eratosthenes to find all prime numbers up to m_num.
    
    Parameters:
    m_num (int): The upper limit to check for prime numbers.
    
    Returns:
    list: A list where index i is True if i is prime, else False.
    """
    i_prime = [True] * (m_num + 1)
    i_prime[0], i_prime[1] = False, False  # 0 and 1 are not prime numbers
    for i in range(2, int(m_num**0.5) + 1):
        if i_prime[i]:
            for j in range(i * i, m_num + 1, i):
                i_prime[j] = False
    return i_prime

def main():
    """
    Main function to process multiple test cases and find a pair of indices 
    (i, j) such that the sum A[i] + A[j] is not prime.
    
    Approach:
    1. Use the Sieve of Eratosthenes to precompute prime numbers up to 200,
       as the maximum possible sum of any two elements from A is 200 (100 + 100).
    2. For each test case:
       - Read the size of the array and the elements.
       - Count the frequency of each number in the array using a frequency list.
       - Iterate through all possible pairs of numbers (i, j) from 1 to 100:
         - Ensure that the pair has at least one occurrence in the frequency list.
         - If i != j, or if i == j, check the frequency to ensure there are at least two instances.
         - Check if the sum (i + j) is not prime using the precomputed prime list.
         - If a valid pair is found, record the indices and print them.
    3. If no valid pair is found after checking all possibilities, output -1.

    Pseudocode:
    - Initialize prime array using Sieve of Eratosthenes up to 200.
    - For each test case:
        - Read N and the array A.
        - Initialize frequency list for numbers 1 to 100.
        - Count occurrences of each number in A.
        - For each pair (i, j):
            - Check frequency and if i + j is not prime.
            - If valid, find indices in A and print them.
    - If no valid pair is found, print -1.

    Time Complexity:
    - Sieve of Eratosthenes: O(m log log m) where m = 200, which is constant.
    - Counting frequency: O(N) for each test case.
    - Finding pairs: O(100^2) in the worst case, leading to O(1) since 100 is constant.
    - Overall: O(T * N) where T is the number of test cases and N is the number of elements in each test case.

    Summary:
    The program efficiently finds a pair of indices (i, j) such that the sum of the corresponding elements 
    in the array is not prime. It handles multiple test cases and uses precomputation of prime numbers 
    to ensure quick checks during the pair evaluations. If no valid pairs are found, it returns -1.
    """
    
    M_SUM = 200  # Maximum possible sum of two elements
    i_prime = sieve(M_SUM)  # Precompute prime numbers up to 200

    T = int(input())  # Number of test cases
    for _ in range(T):
        N = int(input())  # Size of the array A
        freq = [0] * 101  # Frequency array for numbers from 1 to 100
        A = list(map(int, input().split()))  # Read the array

        # Count occurrences of each number in A
        for number in A:
            freq[number] += 1

        found = False  # Flag to check if a valid pair is found

        # Iterate through all pairs of numbers from 1 to 100
        for i in range(1, 101):
            for j in range(i, 101):
                if freq[i] > 0 and freq[j] > 0:  # Both numbers must be present
                    # Check if we can form a valid pair (i, j)
                    if i != j or freq[i] > 1:
                        total = i + j
                        if not i_prime[total]:  # Check if the sum is not prime
                            f_idx, s_idx = -1, -1  # Indices of the first and second elements
                            for k in range(N):
                                if A[k] == i and f_idx == -1:
                                    f_idx = k + 1  # 1-based index
                                elif A[k] == j and (s_idx == -1 or s_idx == f_idx):
                                    s_idx = k + 1  # 1-based index
                                # Check if we have found two different indices
                                if f_idx != -1 and s_idx != -1 and f_idx != s_idx:
                                    print(f_idx, s_idx)
                                    found = True  # A valid pair is found
                                    break
                            if found:
                                break  # Exit the inner loop if a pair is found
            if found:
                break  # Exit the outer loop if a pair is found

        if not found:  # If no valid pair was found, output -1
            print(-1)

if __name__ == "__main__":
    main()
