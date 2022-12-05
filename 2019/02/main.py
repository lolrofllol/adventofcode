file = open('D:\\Development\\GitHub\\adventofcode\\2019\\02\\input.txt', 'r')

prog_str = file.read().split(',')
prog_array = [int(x) for x in prog_str]
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
        print(f'adding {figure_first} and {figure_second}')
        prog_array[storage_pointer_result] = figure_first + figure_second
    elif op_code == 2:
        # mul
        print(f'multiplying {figure_first} and {figure_second}')
        prog_array[storage_pointer_result] = figure_first * figure_second         
    elif op_code == 99:
        # halt
        print(prog_array[0])
        running = False
    else:
        raise Exception('GEHT NICHT')

    pointer += 4
