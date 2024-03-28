#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

with open ("./Input/Names/invited_names.txt") as names:
    names_list = names.read()
lista = names_list.split("\n")
    
with open("./Input/Letters/starting_letter.txt") as file:
    content = file.read()

for n in lista:
    with open("./Output/ReadyToSend/"+n+".txt", mode= "w") as letter:
        letter.write(content.replace("[name]", n))