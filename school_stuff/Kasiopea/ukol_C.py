import os

try:
    input_file = open(os.path.dirname(os.path.abspath(__file__)) + "/input.txt", "r")
    output_file = open(os.path.dirname(os.path.abspath(__file__)) + "/output.txt", "w")

except:
    exit()

output = []

for i in range(int(input_file.readline())):
    jumps = 0
    count = input_file.readline()
    line = [int(x) for x in input_file.readline().split()]

    """if len(line) != count:
        exit()

    else:
        pass"""

    jumps = 1
    x = 1

    for i in range(0, len(line), x):

        #print(line[i])
        x = 0

        for u in range(line[i] + 1, i, -1):

            print(line[u])

            if line[u] > x:
                x = line[u]
                jumps += 1
                print("Jumped!")

    output.append(jumps)

print(output)

for i in range(len(output)):
    output_file.write(str(output[i]) + "\n")