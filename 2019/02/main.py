file = open('D:\\Development\\GitHub\\adventofcode\\2019\\02\\input.txt', 'r')

prog_str = file.read().split(',')

desired_output = 19690720

brute_force = True

while (brute_force):
    for noun in range(100):
        for verb in range(100):
            print(f'testing noun {noun} and verb {verb}...')
            prog_array = [int(x) for x in prog_str]
            prog_array[1] = noun
            prog_array[2] = verb

            pointer = 0
            running = True

            while (running):
                op_code = prog_array[pointer]
                storage_pointer_first = prog_array[pointer+1]
                storage_pointer_second = prog_array[pointer+2]
                storage_pointer_result = prog_array[pointer+3]

                figure_first = prog_array[storage_pointer_first]
                figure_second = prog_array[storage_pointer_second]

                if op_code == 1:
                    # sum
                    # print(f'adding {figure_first} and {figure_second}')
                    prog_array[storage_pointer_result] = figure_first + figure_second
                elif op_code == 2:
                    # mul
                    # print(f'multiplying {figure_first} and {figure_second}')
                    prog_array[storage_pointer_result] = figure_first * figure_second
                elif op_code == 99:
                    # halt
                    # print(prog_array[0])
                    running = False
                else:
                    raise Exception('GEHT NICHT')

                pointer += 4

            if (prog_array[0] == desired_output):
                raise Exception(f'solution found for noun {noun} and verb {verb}')