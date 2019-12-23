import utils

file_name = 'puzzle_inputs/input_2_1.txt'


def prepare_input():
    puzzle_input = utils.open_file(file_name)
    return utils.make_list_from_string(puzzle_input[0], separator=',', integer=True)


class IntCodeComputer:
    def __init__(self, code, noun=0, verb=0):
        self.memory = code
        self.noun = noun
        self.verb = verb
        self.final_output = 0

    def change_noun_and_verb(self):
        self.memory[1] = self.noun
        self.memory[2] = self.verb

    def cumpute_instructions(self, instruction_pointer, param_1, param_2, param_3):
        if instruction_pointer == 1:
            self.memory[param_3] = self.memory[param_1] + self.memory[param_2]
        else:
            self.memory[param_3] = self.memory[param_1] * self.memory[param_2]

    def loop_though_instructions(self, starting_pointer):
        instruction_pointer = self.memory[starting_pointer]
        if instruction_pointer == 99:
            self.final_output = self.memory[0]
        else:
            param_1 = self.memory[starting_pointer + 1]
            param_2 = self.memory[starting_pointer + 2]
            param_3 = self.memory[starting_pointer + 3]
            self.cumpute_instructions(instruction_pointer, param_1, param_2, param_3)
            starting_pointer += 4
            self.loop_though_instructions(starting_pointer)


def restore_program():
    computer = IntCodeComputer(prepare_input(), noun=12, verb=2)
    computer.change_noun_and_verb()
    computer.loop_though_instructions(0)
    print('Final output for restored program is', computer.final_output)


def find_noun_and_verb():
    value_to_find = 19690720
    for i in range(61, 64):
        for j in range(54, 56):
            computer = IntCodeComputer(prepare_input(), noun=i, verb=j)
            computer.change_noun_and_verb()
            computer.loop_though_instructions(0)
            if computer.final_output == value_to_find:
                print('noun is', computer.noun, 'and verb is', computer.verb)
                print('Answer is', 100 * computer.noun + computer.verb)
                break
        else:
            continue
        break


restore_program()
find_noun_and_verb()
