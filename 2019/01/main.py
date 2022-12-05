file = open('D:\\Development\\GitHub\\adventofcode\\2019\\01\\input.txt','r')

sum = 0

for line in file:
    # print(line)
    fuel_req = int(int(line) / 3) - 2
    sum += fuel_req

    additional_fuel_req = fuel_req
    module_sum = 0

    while(additional_fuel_req > 0):
        fuel_iter = int(additional_fuel_req / 3) - 2
        if(fuel_iter <= 0):
            fuel_iter = 0
        print(f'{additional_fuel_req} fuel requires {fuel_iter} more fuel')
        module_sum += fuel_iter
        additional_fuel_req = fuel_iter

    sum += module_sum

print(sum)