"""
This code implements a simple search for inductive and deductive sentences in text.  It uses three regular expression to find these sentences.   It works by first using a regular expression to break up the text into sentences.   Then it searches each sentence for the inductive and deductive words.   Finally it prints out the deductive sentences and the words found in each.
"""

# The program use two standard librarys the regex library and the operating system library if a text file is searched.
import re
import os


# The file Hume.txt contains the text of Hume's An Enquiry Conerning Human Understanding.
f = open('C://Users//aambrioso//Desktop//Hume.txt')
text = f.read()
f.close()


"""
# This is the text that is searched by the program.
text = 
There are surely four sentences in the text.  Is this the first one or the second one?   This is definitely the third one.   This is possibly the last one!
"""


deductive_words = ['Surely', 'surely', 'Certainly', 'certainly', 'Definitely', 'definitely']

inductive_words = ['Maybe', 'maybe', 'Possibly', 'possibly']

d_str = '|'.join(deductive_words)
i_str = '|'.join(inductive_words)

#  This regular expression searches for text containing deductive words.   
d_word_pattern = re.compile(d_str, re.M)

#  This regular expression searches for text containing inductive words.  
i_word_pattern= re.compile(i_str, re.M)

#  This regular expression searches sentences in the text.  
sentence_pattern = re.compile(r'([A-Z][^\.!?]*[\.!?])', re.M)

sentences = sentence_pattern.findall(text)


wordlist = []
sentencelist = []
classlist = []
infolist = []

sentence_count = 0
for s in sentences:
    d_word = d_word_pattern.findall(s)
    i_word = i_word_pattern.findall(s)
    if len(d_word) > 0:
        infolist.append([s,d_word[0],'D'])
    elif len(i_word) > 0:
        infolist.append([s,i_word[0],'I'])
    else:  
        infolist.append([s, None, 'N'])
    sentence_count += 1


# Use a panel data set to display the information
import pandas as pd
for i in infolist:
    sentencelist.append(i[0])
    wordlist.append(i[1])
    classlist.append(i[2])


   
# Create a dataframe with all the information    
data = {'sentences': sentencelist, 'class':classlist, 'word': wordlist}
frame = pd.DataFrame(data)
print('***************************************')
print(frame)
print('***************************************')
print('The deductive sentence(s)')
print(frame[frame['class'] == 'D'])
print('***************************************')
print('The inductive sentence(s)')
print(frame[frame['class'] == 'I'])
