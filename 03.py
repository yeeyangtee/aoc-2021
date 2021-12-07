
input_file = open("03_input.txt", "r")
lines = input_file.read().split('\n')
print('Number of inputs: ', len(lines))

counter = [0] * len(lines[0])
for line in lines:
    for i, char in enumerate(line):
        counter[i] += int(char)

# Part 1
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

# Part 2
def split_by_pos(lines, position):
    '''function takes in a list of lines, and the postition to evaluate
    will return two lists:  the more common group, the less common group and also the more popular digit.'''
    zero_list = []
    one_list = []
    for line in lines:
        if line[position] == '0': zero_list.append(line)
        else: one_list.append(line)
    
    if len(zero_list) == len(one_list): popular = 'equal'
    elif len(zero_list) > len(one_list): popular = 'zero'
    else: popular = 'one'

    return zero_list, one_list, popular

# Do first split
zero_list, one_list, popular = split_by_pos(lines, 0)
if popular == 'zero':
    oxy = zero_list
    cotwo = one_list
else:
    oxy = one_list
    cotwo = zero_list

for i in range(len(lines[0])-1):
    
    if len(oxy) >1 :
        zero_list, one_list, popular = split_by_pos(oxy, i+1)
        if popular == 'zero':   oxy = zero_list
        else:   oxy = one_list
    if len(cotwo)>1:
        zero_list, one_list, popular = split_by_pos(cotwo, i+1)
        if popular == 'zero':   cotwo = one_list
        else:   cotwo = zero_list

print(oxy, cotwo)
print(int(oxy[0],2)*int(cotwo[0],2))