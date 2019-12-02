import os

try:
    input_file = open(os.path.dirname(os.path.abspath(__file__)) + "/input.txt", "r")
    output_file = open(os.path.dirname(os.path.abspath(__file__)) + "/output.txt", "w")

except:
    exit()

output = []

for i in range(int(input_file.readline())):
    count = int(input_file.readline())
    input_list = [int(x) for x in input_file.readline().split(" ")]

    if len(input_list) > count or len(input_list) < count:
        output.append("NE")
        print("smt1")

    else:
        for u in range(1, len(input_list) + 1):

            if input_list[u - 1] == u or input_list[u - 1] == 0:
               
                if u == len(input_list):
                    output.append("ANO")

                else:
                    pass

            else: 
                output.append("NE")
                break

for i in output:
    print(i)
    output_file.write(i + "\n")