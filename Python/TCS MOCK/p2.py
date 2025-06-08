def min_coins(N):
    if N <= 0:
        print("0 0 0 0")  # Edge case: No coins needed for N <= 0
        return

    five_rupee = N // 5  # Max possible ₹5 coins
    remaining = N % 5     # Remaining value after using ₹5 coins

    two_rupee = remaining // 2  # Max possible ₹2 coins
    one_rupee = remaining % 2    # Remaining value after using ₹2 coins

    total_coins = five_rupee + two_rupee + one_rupee  # Total coins used

    print(total_coins, five_rupee, two_rupee, one_rupee)

# Example Usage
N = int(input())  # Take input
min_coins(N)
