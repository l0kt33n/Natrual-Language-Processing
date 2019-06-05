import nltk
import glob

my_string = input()
my_tokens = my_string.split()
my_tokens.sort()

for tok in my_tokens:
    print(tok)

num_tokens = len(my_tokens)

print('')
print('Number of tokens:')
print(num_tokens)


########## Bonus #############

filelist = []
for file in glob.glob("/inaugural/*.txt")
    filelist.append(file)
    with open(file) as f:
        data = f.read()

    sents = nltk.sent_tokenize(data)
    tokens = nltk.word_tokenize(data)
    words = [word for word in tokens if word.isalpha()]
    fd = nltk.FreqDist(words)
    print(file + fd.B(1000))
