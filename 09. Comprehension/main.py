with open("nato_phonetic_alphabet.csv") as content:
    file = content.readlines()

file = [f.replace("\n","") for f in file]

nato = {n.split(',')[0]: n.split(',')[1] for n in file}
nato[" "] = " "

testo = input("Write the word to be translated in NATO alphabet: ")

try:
    new_word = [nato[a.upper()] for a in testo ]
except:
    print('Please inster only letters')
else:
    new_word = [nato[a.upper()] for a in testo ]
    new_word = ', '.join(new_word)
    print(new_word)
