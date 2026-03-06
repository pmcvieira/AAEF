"""
Knapsack Problem - Brute Force / Try and Error Solution
Tries all possible combinations of items and finds the one with maximum value
within the weight capacity constraint.
"""

from itertools import combinations
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





def knapsack_brute_force(items, capacity):
    """
    Solve the 0/1 knapsack problem using brute force (try all combinations).
    
    Args:
        items: List of tuples (weight, value)
        capacity: Maximum weight capacity of the knapsack
    
    Returns:
        Dictionary with:
        - 'max_value': Maximum value achievable
        - 'selected_items': List of selected items (with indices)
        - 'total_weight': Total weight of selected items
        - 'attempts': Number of combinations tried
    """
    
    n = len(items)
    best_value = 0
    best_combination = []
    attempts = 0
    
    # Try all possible combinations of items
    # combinations(range(n), r) generates all ways to choose r items
    for r in range(n + 1):
        for combo in combinations(range(n), r):
            attempts += 1
            
            # Calculate total weight and value for this combination
            total_weight = sum(items[i][0] for i in combo)
            total_value = sum(items[i][1] for i in combo)
            
            # If this combination fits and is better than current best, update
            if total_weight <= capacity and total_value > best_value:
                best_value = total_value
                best_combination = combo
    
    # Calculate total weight of best solution
    total_weight = sum(items[i][0] for i in best_combination)
    
    return {
        'max_value': best_value,
        'selected_items': list(best_combination),
        'total_weight': total_weight,
        'attempts': attempts
    }


def main():
    print("\n" + "=" * 60)
    print("KNAPSACK PROBLEM - BRUTE FORCE SOLUTION")
    print("=" * 60)

    nitems = 20
    print(f"\nGenerating random instance with {nitems} items...")


    items, capacity = make_random_instance(nitems)

    print(f"\nItems (weight, value):")
    for i, (w, v) in enumerate(items):
        print(f"  Item {i}: weight={w}, value={v}")

    print(f"\nKnapsack Capacity: {capacity}")

    start_time = time.time()
    result = knapsack_brute_force(items, capacity)
    elapsed_time = time.time() - start_time

    print(f"\n{'RESULT':-^60}")
    print(f"Maximum Value: {result['max_value']}")
    print(f"Total Weight: {result['total_weight']}")
    print(f"Selected Items: {result['selected_items']}")
    print(f"Total Combinations Tried: {result['attempts']}")
    print(f"Time Taken: {elapsed_time:.6f} seconds")

    if result['selected_items']:
        print(f"\nSelected Items Details:")
        for idx in result['selected_items']:
            w, v = items[idx]
            print(f"  Item {idx}: weight={w}, value={v}")


if __name__ == "__main__":
    main()
