def determine_coins():
    """
    This function determines how many gold coins Chef receives based on the outcome of a football game
    between Chef and Chefina. The player scoring the maximum goals wins and receives a specified amount
    of gold coins, while the loser receives a different specified amount.

    Approach:
    - Read the input values: A (winner's coins), B (loser's coins), X (Chef's goals), Y (Chefina's goals).
    - Compare the goals scored by Chef and Chefina to determine the winner.
      - If Chef's goals (X) are greater than Chefina's goals (Y), Chef wins and receives A coins.
      - If Chef's goals (X) are less than Chefina's goals (Y), Chef loses and receives B coins.
    - Output the number of coins Chef receives based on the result.

    Intuition:
    - The problem is straightforward: it relies on a simple comparison between two scores.
    - Given the constraints (1 ≤ B < A ≤ 10 and 1 ≤ X, Y ≤ 5, X ≠ Y), we can safely determine the outcome without needing to handle edge cases or invalid inputs.
    - This leads to a clear and efficient solution with constant time complexity.

    Input Format:
    The function expects a single line of input with four space-separated integers:
    - A: Coins rewarded to the winner
    - B: Coins rewarded to the loser
    - X: Goals scored by Chef
    - Y: Goals scored by Chefina

    Output:
    The function prints a single integer denoting the number of coins Chef receives.
    """

    # Step 1: Read the input values
    A, B, X, Y = map(int, input().split())

    # Step 2: Determine the number of coins Chef receives based on the scores
    if X > Y:
        coins = A  # Chef wins
    else:
        coins = B  # Chef loses

    # Step 3: Output the result
    print(coins)

# Call the function to execute the program
determine_coins()
