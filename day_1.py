import  utils

fuel_needed_for_modules = []
file_name = 'puzzle_inputs/input_1_1.txt'
extra_fuel_tracker = []


def equate_fuel_needed(mass):
    return (int(mass) // 3) - 2


def count_fuel_recursively(fuel):
    extra_fuel = equate_fuel_needed(fuel)
    if extra_fuel > 0:
        extra_fuel_tracker.append(extra_fuel)
        count_fuel_recursively(extra_fuel)
    else:
        return extra_fuel


def count_fuel():
    puzzle_input = utils.open_file(file_name)
    for mass in puzzle_input:
        fuel_needed_for_modules.append(equate_fuel_needed(mass))
    print('Part one is :', sum(fuel_needed_for_modules))

    for module in fuel_needed_for_modules:
        count_fuel_recursively(module)

    print('Part two is :', sum(extra_fuel_tracker) + sum(fuel_needed_for_modules))


count_fuel()
