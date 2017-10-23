"""
Monty Hall game analysis by simulation
By Dafu Ai  Oct 2017
Tested in Python 3.6.3
"""

import random

# A list of all the doors
doors = [1, 2, 3]

# Indicates whether we are printing the trace information for simulations
trace = False


def simulate(decision_switch, trials):
    """
    Simulate a given number of random games.
    :param trials: number of trials
    :param decision_switch: whether to switch choice
    :return: number of winning games
    """
    wins = 0

    if trace:
        if decision_switch:
            print("## Switching choice:")
        else:
            print("## NOT switching choice:")

    for i in range(trials):
        wins += 1 if simulate_once(decision_switch) else 0

    return wins


def simulate_once(decision_switch):
    """
    Simulate one random game giving a switch decision.
    :param decision_switch: whether to switch choice
    :return: True if win, False otherwise
    """
    door_car = random.randint(1, 3)

    # Goats behind the rest doors
    doors_goats = copy_remove(doors, door_car)

    # Make the first door choice
    first_choice = random.randint(1, 3)

    if door_car == first_choice:
        door_open = random.choice(doors_goats)
        doors_remain = copy_remove(doors_goats, door_open)
        door_last = doors_remain[0]
    else:
        # Here first choice is a goat door
        doors_remain = copy_remove(doors_goats, first_choice)
        door_open = doors_remain[0]

    if trace:
        print("Door(Car) = %d, Choice(Fist) = %d" % (door_car, first_choice))

    if decision_switch:
        # If first choice is a goat door then switching will turns to a car door
        return first_choice in doors_goats
    else:
        # Keep original choice
        return first_choice == door_car


def copy_remove(_list: list, val: object) -> list:
    """
    :param _list: A list
    :param val: Value to remove from the copy of the list
    :return: A copy of the given list without the value specified.
    """
    copy = _list.copy()
    copy.remove(val)
    return copy


def sample_run():
    """
    Gives a sample run of the simulation and some analysis
    """
    from statistics import mean

    tests = 10
    trials = 100000
    wins_keep_list = []
    wins_switch_list = []

    for i in range(tests):
        wins_keep = simulate(False, trials)
        wins_keep_list.append(wins_keep)
        print("%d wins out of %d games (keeping choice)." % (wins_keep, trials))

        wins_switch = simulate(True, trials)
        wins_switch_list.append(wins_switch)
        print("%d wins out of %d games (switching choice)." % (wins_switch, trials))

    print("AVERAGE: Winning rate = %.3f for keeping choice." % (mean(wins_keep_list) / trials))
    print("AVERAGE: Winning rate = %.3f for switching choice." % (mean(wins_switch_list) / trials))


sample_run()
