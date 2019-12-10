import random

alphabet_upper = ["A", "B", "C", "Č", "D", "Ď", "E", "F", "G", "H", "CH", "I", "J", "K", "L", "M", "N", "Ň", "O", "P", "R", "Ř", "S", "Š", "T", "Ť", "U", "Ú", "Ů", "V", "W", "X", "Y", "Z", "Ž"]
alphabet_lower = ["a", "b", "c", "č", "d", "ď", "e", "f", "g", "h", "ch", "i", "j", "k", "l", "m", "n", "ň", "o", "p", "r", "ř", "s", "š", "t", "ť", "u", "ú", "ů", "v", "W", "x", "y", "z", "ž"]

def cryptodecrypto(sentence):

    new_text = ""
    rand = random.randint(1, 32)

    for i in range(len(sentence)):
        if sentence[i] == " ":
            new_text += " "
        
        elif sentence[i] in alphabet_lower:
            if rand >= len(alphabet_lower) - alphabet_lower.index(sentence[i]):
                rand_new = rand - (len(alphabet_lower) - alphabet_lower.index(sentence[i]))
                new_text += alphabet_lower[rand_new]    
            else:
                new_text += alphabet_lower[alphabet_lower.index(sentence[i]) + rand]               
            
        elif sentence[i] in alphabet_upper:
            if rand >= len(alphabet_upper) - alphabet_upper.index(sentence[i]):
                rand_new = rand - (len(alphabet_upper) - alphabet_upper.index(sentence[i]))
                new_text += alphabet_upper[rand_new]    
            else:
                new_text += alphabet_upper[alphabet_upper.index(sentence[i]) + rand]  


    new_text += f" [Počet míst: {rand}]"

    return new_text
while True:
    sentence = str(input("Zadej větu k zašifrování: "))

    if sentence == "" or sentence == " ":
        exit()

    print(cryptodecrypto(sentence))