# coding: utf-8

dirs = {'baby': 129, 'car': 410, 'food': 409, 'health': 406, 'legend': 396, 'life': 409,
		'love': 158, 'news': 409, 'science': 409, 'sexual': 38
}

data_file_number = 0

def MakeAllWordsList(train_datas):
	# 统计词频
	all_words = {}
	for datas in train_datas:
		for word in datas:
			if word in all_words:
				all_words[word] += 1
			else:
				all_words[word] = 0

	print('all_words length: ', len(all_words.keys()))

	all_words_reverse = sorted(all_words.items(), key=lambda x: x[1], reverse=True)
	for word in all_words_reverse:
		print(word[0], '\t', word[1], '\t', len(word[0]))

	all_words_list = [word[0] for word in all_words_reverse if len(word[0])>1]
	return all_words_list

if __name__ == '__main__':
	for data_name, data_number in dirs.items():
		while data_file_number < data_number:
			file = open('./data/raw_data/'+data_name+'/'+str(data_file_number)+'.txt', 
				'r', encoding='utf-8')
			MakeAllWordsList(file)
			for line in file:
				print(line+'\n', end='')
			file.close()
			data_file_number += 1
		data_file_number = 0
