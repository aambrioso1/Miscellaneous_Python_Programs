"""
This code implements a simple search for inductive and deductive sentences in text.  It uses three regular expression to find these sentences.   It works by first using a regular expression to break up the text into sentences.   Then it searches each sentence for the inductive and deductive words.   Finally it prints out the sentences, the words found in each, and whether the sentence is deductive, inductive, or neither.
"""

# The program use two standard librarys the regex library and the operating system library if a text file is searched.
import re
import os

import requests

# Downloads Hume's An Enquiry Concerning Human Understanding for in Project Gutenberg. 
url = 'https://www.gutenberg.org/files/9662/9662.txt'
r = requests.get(url)
r.raise_for_status()
text = response.text

# Saves Hume's text to the hard drive
f1 = open('C:/Users/aambrioso/PycharmProjects/CSV files/Hume.txt',"w") 
f1.write(text) 
f1.close() #to change 


"""
Use this code if text is on the hard drive.
# The file Hume.txt contains the text of Hume's An Enquiry Concerning Human Understanding found in Project Gutenberg.
https://www.gutenberg.org/files/9662/9662.txt
f = open('C://Users//aambrioso//Desktop//Hume.txt')
text = f.read()
f.close()
"""

# This removes space characters and extra spaces.  This is a minimal amount of cleaning.   For example there is a glossary and legal language at the end of the file that should be removed.
text = re.sub(r'\s+',' ', text)
text = re.sub(' +',' ', text)
# text=text.replace('\s+',' ')
# text=text.replace(r' +',' ')
# text = text.replace(r'\n','')
# " ".join(text.split())


# The list of deductives words that the program searches for.
deductive_words = ['Surely', 'surely', 'Certainly', 'certainly', 'Definitely', 'definitely']

inductive_words = ['Likely', 'likely', 'Maybe', 'maybe', 'Possibly', 'possibly']

d_str = '|'.join(deductive_words)
i_str = '|'.join(inductive_words)

#  This regular expression searches for text containing deductive words.   
d_word_pattern = re.compile(d_str, re.M)

#  This regular expression searches for text containing inductive words.  
i_word_pattern= re.compile(i_str, re.M)
"""
This code implements a simple search for inductive and deductive sentences in text.  It uses three regular expression to find these sentences.   It works by first using a regular expression to break up the text into sentences.   Then it searches each sentence for the inductive and deductive words.   Finally it prints out the sentences, the words found in each, and whether the sentence is deductive, inductive, or neither.
Ambrioso Summer 2019
"""

# The program uses two standard librarys the regex library and the operating system library if a text file is searched.
import re
import os

# The requests library is used to download text from a url online.
import requests

# Downloads Hume's An Enquiry Concerning Human Understanding for in Project Gutenberg. 
url = 'https://www.gutenberg.org/files/9662/9662.txt'
r = requests.get(url)
r.raise_for_status()
text = r.text

# Saves Hume's text to the hard drive.   File name will need to be adjusted.
f = open('C:/Users/aambrioso/PycharmProjects/CSV files/Hume.txt',"w") 
f.write(text) 
f.close()


"""
# Use this code if the text you are analyzing is on your  hard drive.  The file philo.txt should contain the text you wish to analyze.

f = open('C://Users//aambrioso//Desktop//philo.txt')
text = f.read()
f.close()
"""

# This code removes space characters and extra spaces.  We do a minimal amount of cleaning.   For example there is a glossary and legal language at the end of the Hume file that should be removed.
text = re.sub(r'\s+',' ', text)
text = re.sub(' +',' ', text)

# The lists of deductives and inductive words that the program searches for.
deductive_words = ['Surely', 'surely', 'Certainly', 'certainly', 'Definitely', 'definitely']

inductive_words = ['Likely', 'likely', 'Maybe', 'maybe', 'Possibly', 'possibly']

# The vertical bar | is used to mean or in regexes.
d_str = '|'.join(deductive_words)
i_str = '|'.join(inductive_words)

#  This regular expression searches for text containing deductive words.   
d_word_pattern = re.compile(d_str, re.M)

#  This regular expression searches for text containing inductive words.  
i_word_pattern= re.compile(i_str, re.M)

#  This regular expression searches for sentences in the text.  
sentence_pattern = re.compile(r'([A-Z][^\.!?]*[\.!?])', re.M)

sentences = sentence_pattern.findall(text)

# Initializing empty lists for storing the information we collect.
wordlist = []
sentencelist = []
classlist = []
infolist = []

#  We search each sentence in the text for our indicator words and collect them in our lists.
sentence_count = 0
for s in sentences:
    d_word = d_word_pattern.findall(s)
    i_word = i_word_pattern.findall(s)
    if len(d_word) > 0:
        infolist.append([s,d_word[0],'Deductive'])
    elif len(i_word) > 0:
        infolist.append([s,i_word[0],'Inductive'])
    else:  
        infolist.append([s, None, 'Neither'])
    sentence_count += 1


# We use a panel data set to display the information.
import pandas as pd
for i in infolist:
    sentencelist.append(i[0])
    wordlist.append(i[1])
    classlist.append(i[2])


# Create a dataframe with all the information    
data = {'SENTENCE': sentencelist, 'CLASS':classlist, 'WORD': wordlist}
frame = pd.DataFrame(data)

# Creates dataframe for deductive sentences and a one for inductive sentences
dframe = frame[frame['CLASS'] == 'Deductive']
iframe = frame[frame['CLASS'] == 'Inductive']

# We save dataframes with sentence of the cleaned text, the deductive sentence, the inductive sentences.
dframe.to_csv('C:/Users/aambrioso/PycharmProjects/CSV files/d_sentences.csv')

iframe.to_csv('C:/Users/aambrioso/PycharmProjects/CSV files/i_sentences.csv')

frame.to_csv('C:/Users/aambrioso/PycharmProjects/CSV files/Hume_stripped.csv')

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
        infolist.append([s,d_word[0],'Deductive'])
    elif len(i_word) > 0:
        infolist.append([s,i_word[0],'Inductive'])
    else:  
        infolist.append([s, None, 'Neither'])
    sentence_count += 1


# Use a panel data set to display the information
import pandas as pd
for i in infolist:
    sentencelist.append(i[0])
    wordlist.append(i[1])
    classlist.append(i[2])


   
# Create a dataframe with all the information    
data = {'SENTENCE': sentencelist, 'CLASS':classlist, 'WORD': wordlist}
frame = pd.DataFrame(data)

# Creates dataframe for deductive sentences and a one for inductive sentences
dframe = frame[frame['CLASS'] == 'Deductive']
iframe = frame[frame['CLASS'] == 'Inductive']

dframe.to_csv('C:/Users/aambrioso/PycharmProjects/CSV files/d_sentences.csv')

iframe.to_csv('C:/Users/aambrioso/PycharmProjects/CSV files/i_sentences.csv')

frame.to_csv('C:/Users/aambrioso/PycharmProjects/CSV files/Hume_stripped.csv')
