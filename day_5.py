import utils

file_name = 'puzzle_inputs/input_5_1.txt'


def prepare_input():
    puzzle_input = utils.open_file(file_name)
    return utils.make_list_from_string(puzzle_input[0], separator=',', integer=True)


class IntCodeComputer:
    def __init__(self, code):
        self.memory = code
        self.final_output = 0
        self.stop = False
        self.instruction_pointer = 0  # index where an instruction starts, contains opcode

    def loop_through_code(self):
        while True:
            opcode = self.memory[self.instruction_pointer]
            if opcode == 99:
                return print('Done')
            else:
                self.perform_instructions(opcode)

    def perform_instructions(self, opcode_and_instructions):
        opcode, mode_1, mode_2, mode_3 = self.parse_opcode(opcode_and_instructions)
        param_1 = self.memory[self.instruction_pointer + 1]
        param_2 = self.memory[self.instruction_pointer + 2]
        param_3 = self.memory[self.instruction_pointer + 3]
        if opcode == '01' or opcode == '02':
            self.compute_one_or_two(opcode, param_1, param_2, param_3, mode_1, mode_2)
        elif opcode == '03':
            self.compute_three(param_1)
        elif opcode == '04':
            self.compute_four(param_1, mode_3)
        elif opcode == '05' or opcode == '06':
            self.compute_five_or_six(opcode, param_1, param_2, mode_1, mode_2)
        elif opcode == '07' or opcode == '08':
            self.compute_seven_or_eight(opcode, param_1, param_2, param_3, mode_1, mode_2)

    @staticmethod
    def parse_opcode(opcode):
        opcode = f"{opcode:05d}"
        real_upcode = opcode[3:]
        mode_param_1 = opcode[2]
        mode_param_2 = opcode[1]
        mode_param_3 = opcode[0]
        return real_upcode, mode_param_1, mode_param_2, mode_param_3

    def compute_one_or_two(self, opcode, param_1, param_2, param_3, mode_1, mode_2):
        first_value = self.memory[param_1] if mode_1 == '0' \
            else param_1
        second_value = self.memory[param_2] if mode_2 == '0' \
            else param_2
        if opcode == '01':
            self.memory[param_3] = first_value + second_value
        else:
            self.memory[param_3] = first_value * second_value
        self.instruction_pointer += 4

    def compute_three(self, param):
        self.memory[param] = 5
        self.instruction_pointer += 2

    def compute_four(self, param, mode):
        value_to_output = self.memory[param] if mode == '0' else param
        print('Output is:', value_to_output, '\n')
        self.instruction_pointer += 2

    def compute_five_or_six(self, opcode, param_1, param_2, mode_1, mode_2):
        first_value = self.memory[param_1] if mode_1 == '0' else param_1
        second_value = self.memory[param_2] if mode_2 == '0' else param_2
        jump = True if (opcode == '05' and first_value != 0) or (opcode == '06' and first_value == 0) else False
        if jump:
            self.instruction_pointer = second_value
        else:
            self.instruction_pointer += 3

    def compute_seven_or_eight(self, opcode, param_1, param_2, param_3, mode_1, mode_2):
        first_value = self.memory[param_1] if mode_1 == '0' else param_1
        second_value = self.memory[param_2] if mode_2 == '0' else param_2
        value = 1 if (opcode == '07' and first_value < second_value) \
                or (opcode == '08' and first_value == second_value) \
                else 0
        self.memory[param_3] = value
        self.instruction_pointer += 4


computer = IntCodeComputer(prepare_input())
computer.loop_through_code()
