file = open('D:\\Development\\GitHub\\adventofcode\\2019\\01\\input.txt','r')

sum = 0

for line in file:
    # print(line)
    fuel_req = int(int(line) / 3) - 2
    sum += fuel_req

print(sum)