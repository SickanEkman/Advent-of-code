valid_passwords_1 = []
valid_passwords_2 = []


def iterate_through_range(inclusive_start, inclusive_stop, part=1):
    for num in range(inclusive_start, inclusive_stop + 1):
        if check_requirements(num):
            if check_increase(num):
                if part == 1:
                    check_adjacent(num)
                else:
                    check_only_two_adjacent(num)


def check_requirements(number):
    if len(str(number)) == 6:
        return True


def check_increase(number):
    for i in range(0, 5):
        try:
            if int(str(number)[i]) > int(str(number)[i + 1]):
                break
        except IndexError:
            break
    else:
        return True


def check_adjacent(number):
    for i in range(0, 5):
        if str(number)[i] == str(number)[i + 1]:  # Two adjacent == good
            valid_passwords_1.append(number)
            break


def check_only_two_adjacent(number):
    hit = False
    for i in range(0, 5):
        two_similar = False
        if str(number)[i] == str(number)[i + 1]:
            two_similar = True
            try:
                if str(number)[i] == str(number)[i + 2]:
                    two_similar = False
            except IndexError:
                pass
            try:
                if str(number)[i] == str(number)[i - 1]:
                    two_similar = False
            except IndexError:
                pass
        else:
            pass
        if two_similar:
            hit = True
    if hit:
        valid_passwords_2.append(number)


iterate_through_range(145852, 616942, part=1)
print('Answer part 1:', len(valid_passwords_1))
iterate_through_range(145852, 616942, part=2)
print('Answer part 2:', len(valid_passwords_2))
