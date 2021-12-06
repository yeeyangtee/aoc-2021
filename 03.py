
input_file = open("03_input.txt", "r")
lines = input_file.read().split('\n')
print('Number of inputs: ', len(lines))

counter = [0] * len(lines[0])
for line in lines:
    for i, char in enumerate(line):
        counter[i] += int(char)


print(counter)
gamma = ''
eps = ''
for bit in counter:
    if bit > 500:
        gamma+='1'
        eps+='0'
    else:
        gamma+='0'
        eps+='1'

print(int(gamma,2) *int(eps,2))


