import nltk

def get_inaugural_data(filename):
    data = nltk.corpus.PlaintextCorpusReader('.', [filename])
    word_counts = len(data.words(filename))
    with open(filename, 'r') as fh:
        for line in fh:
            word_list = line.replace(',','').replace('\'','').replace('.','').lower().split()
    
    fd = nltk.FreqDist(word_list)

    return (word_counts, fd)

def get_avg_sentence_len(filename):
    data = nltk.corpus.PlaintextCorpusReader('.', [filename])
    sents = (nltk.corpus.inaugural.sents(filename))
    total_words = 0

    for words in sents:
        total_words += len(words)
    
    return (total_words / len(words))

def main():
    wash_result = get_inaugural_data('1789-Washington.txt')
    wash_avg_len = get_avg_sentence_len('1789-Washington.txt')
    print ('1789-Washington.txt: ' + str(wash_result[0]) + ' words')
    print(wash_result[1].most_common(20))
    print ("Average sentence length: " + str(wash_avg_len))
    print ('')


if __name__ == '__main__':
    main()