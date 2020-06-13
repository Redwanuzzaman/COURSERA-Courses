import re
file = open("regex_sum_631345.txt")
answer = 0
for line in file:
    line = line.rstrip()
    numbers = re.findall('[0-9]+', line)
    for i in range(len(numbers)):
        numbers[i] = int(numbers[i])
    answer += sum(numbers)

print(answer)

# OUTPUT: 558065
