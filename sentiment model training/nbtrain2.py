import glob
import nltk
import pickle
import os
import sys

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
    
##main()
# Modified from part 1
# Now main() takes in two arguments from the command line:
# arg[1], dirName, specifies a directory where the training date is
# arg[2], saveName, specifies the name of the model file to be saved

def main():
    model = {}
    dirName = sys.argv[1]
    saveName = sys.argv[2]
    classList = next(os.walk(dirName))[1] #from stackoverflow https://stackoverflow.com/questions/800197/how-to-get-all-of-the-immediate-subdirectories-in-python
    
    for label in classList:
        result = train(dirName+'/'+label+'/*')
        model[label+'_count'] = result[0]
        model[label+'_fd'] = result[1]
        
    pickle.dump(model, open(saveName, 'wb'))
    

if __name__ == '__main__':
    main()