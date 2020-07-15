import pickle
import nltk
import glob
import pdb


def calc_p(model):
	num_pos = model['pos_count']
	tokens = model['pos_fd'].N()
	p = {}

	for word in model['pos_fd']:
		num_word = model['pos_fd'][word]
		p.setdefault(word,[0,0])
		p[word][0]=(num_word / tokens)

	num_pos = model['neg_count']
	tokens = model['neg_fd'].N()

	for word in model['neg_fd']:
		num_word = model['neg_fd'][word]
		if word not in p:
			p.setdefault(word,[0,0])
		p[word][1]=(num_word / tokens)

	return p

def predict(p, pred_dir, output_file):
	fileList = glob.glob(pred_dir+'*')
	fileList.sort()
	output = open(output_file, 'w')
	for fname in fileList:
		with open(fname) as f:
			file_prob =  [0,0]
			data = f.read()
			words = nltk.word_tokenize(data)
			for word in words:
				if word not in p:
					p.setdefault(word, [0,0])
				file_prob[0] +=  p[word][0]
				file_prob[1] +=  p[word][1]
			if(file_prob[0]>file_prob[1]):
				print(fname, 'pos', file=output)
			else:
				print(fname, 'neg', file=output)
		f.close()
	output.close()


def main():
	model_file = 'sentiment.nb'
	pred_dir = 'data/dev/'
	output_file = 'prediction.txt'
	model = pickle.load(open(model_file,'rb'))
	train_p = calc_p(model)
	pred_p = predict(train_p, pred_dir, output_file)


if __name__ == '__main__':
    	main()