"""
Knapsack Problem - Dynamic Programming / State-Based Solution
Uses dynamic programming to solve the 0/1 knapsack problem by building up
a table of optimal solutions for subproblems.
"""

import time
import random


def make_random_instance(n: int):
    """Return a random knapsack instance with *n* items and a sensible capacity.

    We generate each item with weight in [1,10] and value in [1,100].  The
    capacity is then set to roughly half the sum of all weights, ensuring the
    problem is neither trivially empty nor trivially full.

    Args:
        n: Number of items to include in the instance.

    Returns:
        A tuple ``(items, capacity)`` where ``items`` is a list of
        ``(weight, value)`` pairs and ``capacity`` is an integer.
    """
    items = [(random.randint(1, 10), random.randint(1, 100)) for _ in range(n)]
    total_weight = sum(w for w, _ in items)
    # choose about half the total weight for capacity
    capacity = total_weight // 2
    if capacity <= 0:
        capacity = 1
    return items, capacity


def knapsack_dp(items, capacity):
    """
    Solve the 0/1 knapsack problem using Dynamic Programming (state-based).
    
    Args:
        items: List of tuples (weight, value)
        capacity: Maximum weight capacity of the knapsack
    
    Returns:
        Dictionary with:
        - 'max_value': Maximum value achievable
        - 'selected_items': List of selected items (with indices)
        - 'total_weight': Total weight of selected items
        - 'states_computed': Number of states computed
    """
    
    n = len(items)
    
    # Create DP table: dp[i][w] = max value using items 0..i-1 with capacity w
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    # Fill the DP table
    states_computed = 0
    for i in range(1, n + 1):
        weight, value = items[i - 1]
        for w in range(capacity + 1):
            states_computed += 1
            
            # Option 1: Don't take item i-1
            dp[i][w] = dp[i - 1][w]
            
            # Option 2: Take item i-1 (if it fits)
            if weight <= w:
                dp[i][w] = max(dp[i][w], dp[i - 1][w - weight] + value)
    
    # Backtrack to find which items were selected
    selected_items = []
    w = capacity
    for i in range(n, 0, -1):
        # If the value came from including item i-1
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(i - 1)
            w -= items[i - 1][0]
    
    selected_items.reverse()
    
    # Calculate total weight
    total_weight = sum(items[i][0] for i in selected_items)
    
    return {
        'max_value': dp[n][capacity],
        'selected_items': selected_items,
        'total_weight': total_weight,
        'states_computed': states_computed
    }


def main():
    print("\n" + "=" * 60)
    print("KNAPSACK PROBLEM - DYNAMIC PROGRAMMING SOLUTION")
    print("=" * 60)

    nitems = 7
    print(f"\nGenerating random instance with {nitems} items...")

    items, capacity = make_random_instance(nitems)

    print(f"\nItems (weight, value):")
    for i, (w, v) in enumerate(items):
        print(f"  Item {i}: weight={w}, value={v}")

    print(f"\nKnapsack Capacity: {capacity}")

    start_time = time.time()
    result = knapsack_dp(items, capacity)
    elapsed_time = time.time() - start_time

    print(f"\n{'RESULT':-^60}")
    print(f"Maximum Value: {result['max_value']}")
    print(f"Total Weight: {result['total_weight']}")
    print(f"Selected Items: {result['selected_items']}")
    print(f"States Computed: {result['states_computed']}")
    print(f"Time Taken: {elapsed_time:.6f} seconds")

    if result['selected_items']:
        print(f"\nSelected Items Details:")
        for idx in result['selected_items']:
            w, v = items[idx]
            print(f"  Item {idx}: weight={w}, value={v}")

if __name__ == "__main__":
    main()
