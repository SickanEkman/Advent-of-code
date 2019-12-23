import utils

file_name = 'puzzle_inputs/input_3_1.txt'


def prepare_input():
    puzzle_input = utils.open_file(file_name)
    w_1 = utils.make_list_from_string(puzzle_input[0], separator=',')
    w_2 = utils.make_list_from_string(puzzle_input[1], separator=',')
    return w_1, w_2


class Grid:
    def __init__(self, w1, w2):
        self.w1 = w1
        self.w2 = w2
        self.w1_cells = self.walk_the_wire(w1)
        self.w2_cells = self.walk_the_wire(w2)
        self.w1_cells_as_set = set(self.w1_cells)
        self.w2_cells_as_set = set(self.w2_cells)
        self.intersections = self.w1_cells_as_set.intersection(self.w2_cells_as_set)
        self.minimal_manhattan_distance = min(abs(i[0]) + abs(i[1]) for i in self.intersections)
        self.count_steps()

    def walk_the_wire(self, wire):
        current_position = (0, 0)
        cell_to_add = (0, 0)
        cells_passed = []
        for direction in wire:
            number_of_steps = int(direction[1:])
            if direction.startswith('R') or direction.startswith('D'):
                for num in range(1, number_of_steps + 1):
                    if direction.startswith('R'):
                        cell_to_add = (current_position[0], current_position[1] + num)
                    elif direction.startswith('D'):
                        cell_to_add = (current_position[0] + num, current_position[1])
                    cells_passed.append(cell_to_add)
            elif direction.startswith('L') or direction.startswith('U'):
                for num in range(-1, -(number_of_steps + 1), -1):
                    if direction.startswith('L'):
                        cell_to_add = (current_position[0], current_position[1] + num)
                    elif direction.startswith('U'):
                        cell_to_add = (current_position[0] + num, current_position[1])
                    cells_passed.append(cell_to_add)
            current_position = cell_to_add
        return cells_passed

    def count_steps(self):
        number_steps = []
        for cell in self.intersections:
            w1_steps = self.w1_cells.index(cell)
            w2_steps = self.w2_cells.index(cell)
            total_steps = w1_steps + w2_steps + 2
            number_steps.append(total_steps)
        return min(number_steps)


wire_1, wire_2 = prepare_input()

grid = Grid(wire_1, wire_2)
grid.count_steps()
print('Answer 1, manhattan distance:', grid.minimal_manhattan_distance)

answer_two = grid.count_steps()
print('Answer 2, minimum steps:', answer_two)
