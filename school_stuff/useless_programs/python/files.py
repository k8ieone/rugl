def read_file():
    new_list = []
    with open("vstupA.txt", "r") as f:
        new_list.append((f.readline()))
    data = new_list[0].split()
    return data

def separate_lists(list1):
    list_pos = []
    list_neg = []
    for item in list1:
        if int(item) >= 0:
            list_pos.append(int(item))
        elif int(item) < 0:
            list_neg.append(int(item))
    return [list_pos, list_neg]

def output(list1):
    with open("output_Medved.txt", "w") as f:
        for item in list1[0]:
            f.write(str(item) + " ")
        f.write("\n")
        for item in list1[1]:
            f.write(str(item) + " ")

output(separate_lists(read_file()))

def strip_stuff(list1):
    new_list_neg = []
    new_list_pos = []
    def_list = "smt"
    counter = 1
    neg_counter = 1
    for item in list1:
        new_thing = item.strip()
    for item in new_thing:
        if item == "-":
            def_list = "new_list_neg"
            neg_counter += 1
            
        else:
            def_list = "new_list_pos"
            counter += 1
            
        if item == " " and def_list == "smt" or item == "" and def_list == "smt":
            new_list_pos.append("")
            new_list_neg.append("")
            counter += 1
            counter_neg += 1
            
        elif def_list == "new_list_pos" and item == " ":
            new_list_pos.append("")
        elif def_list == "new_list_neg" and item == " ":
            new_list_neg.append("")
            
        elif def_list == "new_list_pos":
            new_list_pos[counter].append(item)
            
        elif def_list == "new_list_neg":
            new_list_neg[neg_counter].append(item)
            
    return [new_list_pos, new_list_neg]

# print(strip_stuff(list2))
