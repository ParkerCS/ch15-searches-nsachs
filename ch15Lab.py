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
    dictionary_list.append(line.strip())
file.close()

print("------Linear Search------")

file2 = open("AliceInWonderLand200.txt", "r")
text_list = []
def spell_check(file2):
    for line in file2:
        words = split_line(line)
        #text_list.append(words)
        for word in words:
            key = word.upper()
            for i in range(len(dictionary_list)):
                #print(dictionary_list[i])
                if dictionary_list[i] == key:
                    break
            else:
                print(key, "is not found.")

spell_check(file2)
print()

print("------Binary Search------")

file3 = open("AliceInWonderLand200.txt", "r")

found = False

for line in file3:
    line_number = 0
    lower_bound = 0
    upper_bound = len(dictionary_list) - 1
    words = split_line(line)
    line_number += 1
    for word in words:
        key = word.upper()
        while lower_bound <= upper_bound and not found:
            middle_position = (lower_bound + upper_bound) // 2
            if dictionary_list[middle_position].upper() < key.upper():
                lower_bound += middle_position + 1
            elif dictionary_list[middle_position].upper() > key.upper():
                upper_bound -= middle_position - 1
            else:
                found = True
                #print(word,'on line number', line_number, 'was not found in the dictionary.')
        if not found:
            print(word, "on line number", line_number, "was not found in the dictionary.")


file3.close()

#Not quite sure why it doesn't fully work
