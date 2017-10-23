# Dafu Ai

import random

doors = [1, 2, 3]
trace = False


def simulate(decision_switch, trials):
    wins = 0

    for i in range(trials):
        wins += 1 if simulate_once(decision_switch) else 0

    return wins


def simulate_once(decision_switch):
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
        print("car = %d, first = %d" % (door_car, first_choice))

    if decision_switch:
        # If first choice is a goat door then switching will turns to a car door
        return first_choice in doors_goats
    else:
        # Keep original choice
        return first_choice == door_car


def copy_remove(_list, val):
    copy = _list.copy()
    copy.remove(val)
    return copy


print(simulate(False, 1000))
