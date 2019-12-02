output_final = []

for i in range(int(input())):
    matrix = []
    temp_input = [int(x) for x in input().split()]
    # n je na pozici 0
    # m je na pozici 1

    for u in range(temp_input[0]):
        semi_matrix = [int(x) for x in input().split()]

        if len(semi_matrix) != temp_input[1]:
            exit()

        else:
            matrix.append(semi_matrix)

    numbers = matrix[0]
    print(numbers)

    for u in range(1, len(matrix)):
        for o in range(len(matrix[u])):

            if  numbers[o] == 1 and matrix[u][o] == 1: 
                numbers[o] = 1
                print("logic0")
            elif numbers[o] == 1 and matrix[u][o] == 0: 
                numbers[o] = 1
                print("logic1")
            elif numbers[o] == 0 and matrix[u][o] == 1: 
                numbers[o] = 1
                print("logic2")
            else:                                       
                numbers[o] = 0
                print("logic3")
                
print(numbers)