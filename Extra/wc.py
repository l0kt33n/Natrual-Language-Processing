FILE_NAME = '84-0.txt'

wordCounter = {}
fulllist = {}
with open(FILE_NAME,'r') as fh:
  for line in fh:
    # Replacing punctuation characters. Making the string to lower.
    # The split will spit the line into a list.
    word_list = line.replace(',','').replace('\'','').replace('.','').lower().split()
    for word in word_list:
      # Adding  the word into the wordCounter dictionary.
      if word not in wordCounter:
        wordCounter[word] = 1
        fulllist[word] = [wordCounter[word]]
      else:
        # if the word is already in the dictionary update its count.
        wordCounter[word] = wordCounter[word] + 1
        fulllist[word] = [wordCounter[word]]

sortedlist = sorted(fulllist.items() , reverse=True, key=lambda x: x[1])
 
# Iterate over the sorted sequence
print(FILE_NAME)
print("====================")
i = 0
for word in sortedlist :
    if i < 20:
      print(i+1, " " , word[0] , ": " , word[1]) 
      i = i + 1   
print("====================")
FILE_NAME = '2600-0.txt'

wordCounter = {}
fulllist = {}
with open(FILE_NAME,'r') as fh:
  for line in fh:
    # Replacing punctuation characters. Making the string to lower.
    # The split will spit the line into a list.
    word_list = line.replace(',','').replace('\'','').replace('.','').lower().split()
    for word in word_list:
      # Adding  the word into the wordCounter dictionary.
      if word not in wordCounter:
        wordCounter[word] = 1
        fulllist[word] = [wordCounter[word]]
      else:
        # if the word is already in the dictionary update its count.
        wordCounter[word] = wordCounter[word] + 1
        fulllist[word] = [wordCounter[word]]

sortedlist = sorted(fulllist.items() , reverse=True, key=lambda x: x[1])
 

print(FILE_NAME)
print("====================")
i = 0
for word in sortedlist :
    if i < 20:
      print(i+1, " " , word[0] , ": " , word[1]) 
      i = i + 1   
print("====================")
FILE_NAME = 'pg105.txt'

wordCounter = {}
fulllist = {}
with open(FILE_NAME,'r') as fh:
  for line in fh:
    # Replacing punctuation characters. Making the string to lower.
    # The split will spit the line into a list.
    word_list = line.replace(',','').replace('\'','').replace('.','').lower().split()
    for word in word_list:
      # Adding  the word into the wordCounter dictionary.
      if word not in wordCounter:
        wordCounter[word] = 1
        fulllist[word] = [wordCounter[word]]
      else:
        # if the word is already in the dictionary update its count.
        wordCounter[word] = wordCounter[word] + 1
        fulllist[word] = [wordCounter[word]]

sortedlist = sorted(fulllist.items() , reverse=True, key=lambda x: x[1])
 
# Iterate over the sorted sequence
print(FILE_NAME)
print("====================")
i = 0
for word in sortedlist :
    if i < 20:
      print(i+1, " " , word[0] , ": " , word[1]) 
      i = i + 1   
print("====================")
FILE_NAME = 'pg1661.txt'

wordCounter = {}
fulllist = {}
with open(FILE_NAME,'r') as fh:
  for line in fh:
    # Replacing punctuation characters. Making the string to lower.
    # The split will spit the line into a list.
    word_list = line.replace(',','').replace('\'','').replace('.','').lower().split()
    for word in word_list:
      # Adding  the word into the wordCounter dictionary.
      if word not in wordCounter:
        wordCounter[word] = 1
        fulllist[word] = [wordCounter[word]]
      else:
        # if the word is already in the dictionary update its count.
        wordCounter[word] = wordCounter[word] + 1
        fulllist[word] = [wordCounter[word]]

sortedlist = sorted(fulllist.items() , reverse=True, key=lambda x: x[1])
 
# Iterate over the sorted sequence
print(FILE_NAME)
print("====================")
i = 0
for word in sortedlist :
    if i < 20:
      print(i+1, " " , word[0] , ": " , word[1]) 
      i = i + 1   

