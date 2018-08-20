# coding: utf-8

import os
import time
import random
import jieba
import nltk
import sklearn
from sklearn.naive_bayes import MultinomialNB
import numpy as np 
import pylab as pl 
import matplotlib.pyplot as plt 


def MakeWordsSet(words_file):
	words_set = set()
	with open(words_file, 'r', encoding='utf-8') as fp:
		for line in fp.readlines():
			word = line.strip()
			if len(word)>0 and word not in words_set:
				words_set.add(word)
	return words_set


def TextProcessing(folder_path, test_size=0.2):
	folder_list = os.listdir(folder_path)
	data_list = []
	class_list = []

	for folder in folder_list:
		# './data/demo/car'
		new_folder_path = os.path.join(folder_path, folder)
		# ['0.txt', '1.txt', ...]
		files = os.listdir(new_folder_path)

		j = 0
		for file in files:
			if j > 410:
				break
			# ./data/demo/car/0.txt
			filename = os.path.join(new_folder_path, file)
			with open(filename, 'r', encoding='utf-8') as fp:
				raw_data = fp.read()
			print(raw_data)
			word_cut = jieba.cut(raw_data, cut_all=False)
			word_list = list(word_cut)
			print(word_list)
			data_list.append(word_list) # [[词集1],[词集2], ...]
			class_list.append(folder) # ['car', 'baby', ...]

	# 划分训练集和测试集
	data_class_list = list(zip(data_list, class_list)) # [(['词集1'], 'car'),(['词集2'], 'car')...]
	random.shuffle(data_class_list) # 打乱次序
	index = int(len(data_class_list) * test_size) + 1 # 分割点
	train_list = data_class_list[index:] # 训练词汇集  [(['词集1'], 'car'),(['词集2'], 'car')...]
	test_list = data_class_list[:index] # 测试词汇集	[(['词集1'], 'car'),(['词集2'], 'car')...]
	train_data_list, train_class_list = zip(*train_list) # 词类分开(生成器) (['词集2'], ['词集6'],...), ('car', 'car', ...)
	test_data_list, test_class_list = zip(*test_list)	# 词类分开(生成器) (['词集6'], ['词集6'],...), ('car', 'car', ...)

	# 统计词频放入all_words_dict
	all_words_dict = {}						# 统计所有分类里的所有词的个数
	for word_list in train_data_list:  
		for word in word_list:				# word: ['词1', '词2', ..]
			if word in all_words_dict:		
				all_words_dict[word] += 1
			else:
				all_words_dict[word] = 0

	all_words_list = sorted(all_words_dict.items(), key=lambda x: x[1], reverse=True) # [('词1', 10), ('词2', 5), ...]
	all_words_list = list(zip(*all_words_list))[0]  # 训练的词汇 ['词1', '词2',...]
	
	# 	 ['词1', '词2', ..] (['词集2'], ...) (['词集8'], ..)  (['词集2'], ...)   (['词集2'], ...)
	return all_words_list, train_data_list, test_data_list, train_class_list, test_class_list


def words_dict(all_words_list, deleteN, stopwords_set=set()):
	# 选取特征词
	feature_words = []
	n = 1
	for t in range(deleteN, len(all_words_list), 1):
		if n > 10000:
			break
		# all_words_list: ['词1', '词2', ..]      stopwords_set: {'停词1', '停词2', ...}
		if not all_words_list[t].isdigit() and all_words_list[t] not in stopwords_set and \
			1 < len(all_words_list[t]) < 5:
			feature_words.append(all_words_list[t])		# 添加特征词
			n += 1
	return feature_words		# ['特征值1', '特征值2', ...]


def TextFeatures(train_data_list, test_data_list, feature_words, flag='nltk'):
	# train_data_list: (['词集2'], ...)      feature_words: ['特征值1', '特征值2', ...]
	def text_features(text, feature_words):
		'''
		text: ['词集1']
		feature_words: ['特征值1', '特征值2', ...]
		'''
		text_words = set(text)
		if flag == 'nltk':
			# text中的值在特征值集中,表示为1, 否则为0
			features = {word: 1 if word in text_words else 0 for word in feature_words}
		elif flag == 'sklearn':
			features = [1 if word in text_words else 0 for word in feature_words]
		else:
			features = []
		return features

	train_feature_list = [text_features(text, feature_words) for text in train_data_list]
	test_feature_list = [text_features(text, feature_words) for text in test_data_list]

	return train_feature_list, test_feature_list


def TextClassifier(train_feature_list, test_feature_list, train_class_list, test_class_list,
					flag='nltk'):
	'''
	train_feature_list: [1, 0, 1, 1, ...]
	train_class_list: ['car', 'car', 'baby', ...] 
	'''

	if flag == 'nltk':
		train_flist = zip(train_feature_list, train_class_list) # [(1, 'car'), ...]
		test_flist = zip(test_feature_list, test_class_list) # [(1, 'car'), ...]
		classifier = nltk.classify.NaiveBayesClassifier.train(train_flist) 
		test_accuracy = nltk.classify.accuracy(classifier, train_flist)
	elif flag == 'sklearn':
		# 训练集合进行训练,估计参数
		classifier = MultinomialNB().fit(train_feature_list, train_class_list)
		print(classifier.predict(text_feature_list))
		for test_feature in test_feature_list:
			print(classifier.predict(test_feature)[0])
		# 准确率
		test_accuracy = classifier.score(test_feature_list, test_class_list)
	else:
		test_accuracy
	return test_accuracy

if __name__ == '__main__':
	print('start')

	folder_path = './data/demo'
	# {'词1': 2,...} (['词集2'], ...) (['词集8'], ..)  (['词集2'], ...)   (['词集2'], ...)
	all_words_list, train_data_list, test_data_list, train_class_list, test_class_list = TextProcessing(folder_path, test_size=0.2)

	stopwords_file = './data/stopword.txt'
	stopwords_set = MakeWordsSet(stopwords_file)

	# 文本特征提取和分类
	flag = 'sklearn'
	deleteNs = range(0, 1000, 20)
	test_accuracy_list = []
	for deleteN in deleteNs:
		feature_words = words_dict(all_words_list, deleteN, stopwords_set)
		train_feature_list, test_feature_list = TextFeatures(train_data_list, test_data_list, feature_words, flag)
		test_accuracy = TextClassifier(train_feature_list, test_feature_list, train_class_list, test_class_list, flag)
		test_accuracy_list.append(test_accuracy)
	print(test_accuracy_list)

	# 结果
	plt.figure()
	plt.plot(deleteNs, test_accuracy_list)
	plt.title('Relationship of deleteNs and test_accuracy')
	plt.xlabel('deleteNs')
	plt.ylabel('test_accuracy')
	plt.savefig('result_news.png')

	print('finished')


