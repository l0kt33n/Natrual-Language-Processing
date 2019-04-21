import nltk
import string

def process_wc_top_avglen(filename):
    with open(filename) as f:
        data = f.read()

    
    sents = nltk.sent_tokenize(data)
    tokens = nltk.word_tokenize(data)
    words = [word for word in tokens if word.isalpha()]
    fd = nltk.FreqDist(words)

    total_words = len(tokens)
    
    avg_sent_len = total_words / len(sents)

    return (total_words, fd, avg_sent_len)

def print_wc_top_avglen(filename):
    result = process_wc_top_avglen(filename)
    avg_len = round(result[2], 2)
    print (filename)
    print ('word count: ' + str(result[0]) + ' words')
    print(result[1].most_common(20))
    print ("Average sentence length: " + str(avg_len))
    print ('')

def main():
    print_wc_top_avglen('1789-Washington.txt')
    print_wc_top_avglen('2009-Obama.txt')
    print_wc_top_avglen('2017-Trump.txt')


if __name__ == '__main__':
    main()