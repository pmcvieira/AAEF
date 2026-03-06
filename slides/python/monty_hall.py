"""
Monty Hall simulation showing that switching doors increases probability
of winning. Run as a script to simulate many trials and compare strategies.
"""

import random


def simulate(n_trials: int = 10000) -> dict:
    """Simulate the Monty Hall game.

    Args:
        n_trials: number of random games to play.
    Returns:
        A dictionary with counts for wins when staying vs switching.
    """
    stay_wins = 0
    switch_wins = 0

    for _ in range(n_trials):
        # randomly place prize behind one of three doors
        prize_door = random.randrange(3)
        # contestant makes a choice
        choice = random.randrange(3)

        # host opens a door that is neither the contestant's choice nor the prize
        remaining = [d for d in range(3) if d != choice and d != prize_door]
        host_opens = random.choice(remaining)

        # if contestant stays
        if choice == prize_door:
            stay_wins += 1
        # if contestant switches, switch to the only other closed door
        switch_choice = next(d for d in range(3) if d not in {choice, host_opens})
        if switch_choice == prize_door:
            switch_wins += 1

    return {
        "trials": n_trials,
        "stay_wins": stay_wins,
        "switch_wins": switch_wins,
    }


def main():

    trials = 100000

    results = simulate(trials)
    stay_pct = results["stay_wins"] / results["trials"] * 100
    switch_pct = results["switch_wins"] / results["trials"] * 100

    print("Monty Hall Simulation")
    print("Trials:", results["trials"])
    print(f"Stay wins: {results['stay_wins']} ({stay_pct:.2f}%)")
    print(f"Switch wins: {results['switch_wins']} ({switch_pct:.2f}%)")
    print()
    print("Conclusion: switching wins about twice as often as staying")


if __name__ == "__main__":
    main()
