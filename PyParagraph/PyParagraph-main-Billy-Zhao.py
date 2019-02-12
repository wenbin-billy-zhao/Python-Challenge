import re
import os

selection = input('Please choose which file to summarize: [1] or [2]')

if selection == '1':
    filename = 'raw_data/paragraph_1.txt'
elif selection == '2':
    filename = 'raw_data/paragraph_2.txt'
else:
    input(f'try again, select [1] or [2]')
    
print(f"user selected: {filename}")
file = open(filename, 'r')

text = file.read()

letter_count = sum(c.isalpha() for c in text)

sentence_readout = re.split("(?<=[.!?]) +", text)
# word_readout = re.split(" ", text)
word_count = len(text.split(' '))

print('Paragraph Analysis')
print('-'*60)

# word_count = len(word_readout)
print(f"Approximate Word Count: {word_count}")

sentence_count = len(sentence_readout)
print(f"Approximate Sentence Count : {sentence_count}")

print("Average letter count: " + str(round(letter_count/word_count,2)))

print(f"Average Sentence Length: {word_count / sentence_count}")