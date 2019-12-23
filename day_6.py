import utils


file_name = 'puzzle_inputs/input_6_1.txt'
input_list = utils.remove_new_line_from_list_items(utils.open_file(file_name))


def create_dictionary(input_as_list):
    orbitdict = {}
    for i in input_as_list:
        orbited = i[:3]
        orbitor = i[4:]
        orbitdict[orbitor] = orbited
    return orbitdict


def count_orbits(key, counter, orbitdict):
    if orbitdict.get(key) is not None:
        counter += 1
        return count_orbits(orbitdict[key], counter, orbitdict)
    else:
        return counter


def loop_and_count_all_orbits(orbitdict):
    connection_counter = 0
    for keys in orbitdict.keys():
        connection_counter += count_orbits(keys, 0, orbitdict)
    return connection_counter


def list_orbits(orbitdict, starting_point, path):
    if orbitdict.get(starting_point) is not None:
        path.add(orbitdict.get(starting_point))
        return list_orbits(orbitdict, orbitdict[starting_point], path)
    else:
        return path


def find_shortest_path_to_com(orbitdict, starting_point):
    path = set()
    shortest_path_to_com = list_orbits(orbitdict, starting_point, path)
    return shortest_path_to_com


if __name__ == "__main__":
    orbits = create_dictionary(input_list)
    checksum = loop_and_count_all_orbits(orbits)
    print('PART 1, Checksum:', checksum)
    my_path_to_com = find_shortest_path_to_com(orbits, 'YOU')
    santas_path_to_com = find_shortest_path_to_com(orbits, 'SAN')
    shortest_path = my_path_to_com.symmetric_difference(santas_path_to_com)
    print('PART 2, Shortest path:', len(shortest_path))
