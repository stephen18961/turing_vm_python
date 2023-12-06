from poland import parse, evaluate, parse_words
from collections import defaultdict 

def turingVM(program):
    memory = defaultdict(None)
    
    read_start = program[0]
    start = True if read_start == 'start' else False
    
    end = False
    instruction_index = 1 if start else None

    while start and end == False:
        # print(type(instruction_index), instruction_index)
        instruction = parse(program[instruction_index])

        command = instruction[0]

        if command == 'end':
            end = True

        if command == '=':
            # Lakukan operasi polandia dan masukkan ke memory
            target_memory_to_set = instruction[1]
            poland_calculation = evaluate(instruction[2])
            memory[target_memory_to_set] = poland_calculation

        elif command == 'M':
            # Check atau Alter memory
            token = parse_words(program[instruction_index])
            instruction = [item for item in token if item not in ('(', ')')]
            
            if instruction[1] == 'IF':
                # i 0    1     2    3    4    5       6
                # ['M', 'IF', '>', '0', '1', 'goto', '6']
                comparator = instruction[2]
                condition = False
                # check the comparator
                if comparator == '>':
                    if (memory[int(instruction[3])] > memory[int(instruction[4])]):
                        condition = True
                elif comparator == '<':
                    if (memory[int(instruction[3])] < memory[int(instruction[4])]):
                        condition = True
                # komparasi memory berhasil
                if condition:
                    if instruction[5] == 'goto':
                        instruction_index = int(instruction[6])
                        continue

            elif instruction[1] == '+':
                # ['M', '+', '2', '1']
                memory[int(instruction[2])] += memory[int(instruction[3])]
            elif instruction[1] == '-':
                memory[int(instruction[2])] -= memory[int(instruction[3])]
            elif instruction[1] == '*':
                memory[int(instruction[2])] *= memory[int(instruction[3])]
            elif instruction[1] == '/':
                memory[int(instruction[2])] /= memory[int(instruction[3])]
            elif instruction[1] == '=':
                memory[int(instruction[2])] = memory[int(instruction[3])]

        elif command == 'goto':
            instruction_index = int(instruction[1])

        print(memory)
        instruction_index += 1


if __name__ == "__main__":
    program = {
    0: 'start',
    1: "(= 0 (* 3 (+ 1 2)))",
    2: "(= 1 (* 3 (+ 0 2)))",
    3: "M(IF (> 0 1) (goto 6) )",
    4: "M(+ 2 (1))",
    5: "(goto 7)",
    6: "M(= 2 (1))",
    7: '(end)'
    }

    turingVM(program)