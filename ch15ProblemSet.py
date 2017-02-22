'''
Complete the following 3 searching problems using techniques
from class and from Ch15 of the textbook website
'''

#1.  (7pts) Write code which finds and prints the longest
# word in the provided dictionary.  If there are more
# than one longest word, print them all.
import re
file = open("dictionary.txt", "r")
highest = 0

for word in file:
    if (len(word)) >= highest:
        highest = len(word)
        longest_word = word
print(longest_word)


#2.  (10pts)  Write code which finds
# The total word count AND average word length
# in "AliceInWonderLand.txt"

import re
#Number of words in text
def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)

file = open("AliceInWonderLand.txt", "r")
text_list = []

for line in file:
    words = split_line(line)
    for word in range(len(words)):
        text_list.append(words[word])
print("There are", len(text_list), "words in Alice In Wonderland.")

#Average length of words in text
word_length = 0
for i in range(len(text_list)):
    word_length += len(text_list[i])
average_length =word_length // len(text_list)
print("The average word length is", average_length, "letters.")

# CHOOSE ONE OF THE FOLLOWING TWO PROBLEMS

#3 (13pts)  How many times does "Cheshire" occur in"AliceInWonderLand.txt"?
# How many times does "Cat" occur?
# How many times does "Cheshire" immediately followed by "Cat" occur?

#### OR #####

#3  (13pts)Find the most frequently occurring
# seven letter word in "AliceInWonderLand.txt"

def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)

file = open("AliceInWonderLand.txt")
text_list = []
sevens = 0
for line in file:
    words = split_line(line)
    for word in range(len(words)):
        text_list.append(words[word])
        if len(text_list[word]) == 7:
            sevens += 1
print("There are", sevens, "words with seven letters in Alice In Wonderland!")

# Challenge problem (for fun).  What words appear in the text of "Alice in Wonderland" that DO NOT occur in "Alice Through the Looking Glass".  Make a list.  You can substitute this for any of the above problems.



