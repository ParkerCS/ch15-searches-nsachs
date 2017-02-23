'''
Complete the chapter lab at http://programarcadegames.com/index.php?chapter=lab_spell_check
'''
import re

def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)

#Opening and closing dicitonary and adding it to a list
file = open("dictionary.txt", "r")
dictionary_list = []
for line in file:
    dictionary_list.append(line)
file.close()

print("------Linear Search------")

file2 = open("AliceInWonderLand200.txt")
text_list = []
def spell_check(file2):
    for line in file2:
        words = split_line(line)
        text_list.append(words)
        for word in words:
            #text_list.append(word)
            key = word.upper()
            while line in dictionary_list != key:
                print(line, "is an incorrect word.")


#found = True
#while not found:
#print(word.upper)

spell_check(file2)

'''
            key = file2

            # cycle through index while it is not == key and check it i is less that len(list)
            while word[words] != key and words < len(words):
                words += 1

            if words < len(word):
                print("Found", key, "at position", words)  # that means you found it at position
            else:
                print("Key is not in list")  # else means you didn't find it
'''

print("------Binary Search------")

