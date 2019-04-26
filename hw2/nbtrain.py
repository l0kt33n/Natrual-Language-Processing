import glob
import nltk
import pickle


##openFiles(path)
# This function takes in the name of the path
# and return a list of names of all files in the path
def openFiles(path):
    return glob.glob(path)


##readFiles(fileList)
# This function takes the list of file names, tokenize all the text in the list 
# into one list, and return the FreqDist among all text in the list
def readFiles(fileList):
    tokens = []
    for file in fileList:
        with open(file) as f:
            data = f.read()
        words = nltk.word_tokenize(data)
        tokens = tokens + words

    fd = nltk.FreqDist(tokens)
    return fd
    
##train(path)
# This function takes in a path name, and calls openFiles(path) and 
# readFiles(path), and return the training data (count, fd) of the files in the path
def train(path):
    fileList = openFiles(path)
    fd = readFiles(fileList)
    return (len(fileList), fd)
    

def main():
    pos = train('data/train/pos/*')
    neg = train('data/train/neg/*')
    model = {
        'pos_count': pos[0],
        'neg_count': neg[0],
        'pos_fd': pos[1],
        'neg_fd': neg[1]
    }
    pickle.dump(model, open('sentiment.nb', 'wb'))
    

if __name__ == '__main__':
    main()