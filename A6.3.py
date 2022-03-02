#assignment 6.3
#Tristan Werden
#TODO: None
#NOTES:


def count(word, letter):
    count = 0
    for char in word :
        if char == letter :
            count = count + 1
    print(count)


word = input("Please input a string: ")
letter = input("Please input a letter: ")
count(word, letter)
