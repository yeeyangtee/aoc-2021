def get_increments(depths):
    larger = 0
    for i in range(len(depths)-1):
        if int(depths[i+1])>int(depths[i]):
            larger +=1
            # print(depths[i+1])
    return larger

def get_increments_window(depths):
    larger = 0
    for i in range(len(depths)-3):
        if int(depths[i+3])>int(depths[i]):
            larger +=1
    return larger

input_file = open("01_input.txt", "r")
lines = input_file.read().split('\n')
print('Number of inputs: ', len(lines))

print('Number of direct increments: ', get_increments(lines))
print('Number of 3-window increments: ', get_increments_window(lines))
