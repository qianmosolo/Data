# coding: utf-8

import numpy as np
from numpy import *
import operator
from matplotlib.font_manager import FontProperties
import matplotlib.pyplot as plt 
import matplotlib.lines as mines

def createDataSet():
	# 生成一个矩阵,每一行为一个样品
	group = array([[1.0, 0.9], [1.0, 1.0], [0.1, 0.2], [0.0, 0.1]])
	# 样本的所属类别
	labels = ['A', 'A', 'B', 'B']
	return group, labels


def knnClassify(newInput, dataSet, labels, k):
	'''
	newInput:	(1*N)待分类的
	dataSet:	(M*N)训练数据
	labels:		训练数据标签
	k:			邻近数
	return:		可能性最大的分类标签
	'''
	# step1: 计算距离(闵科夫斯基距离)
	# (1)求差
	# [1, 0] - [1, 2]   [0, -2]
	# [2, 3] - [1, 2] = [1,  1]
	# [1, 6] - [1, 2]   [0,  4]
	# (2)差值平方
	# [0,  4]
	# [1,  1]
	# [0, 16]
	# (3)差值平方累积
	# [4]
	# [2]
	# [16]
	# (4) 开平方,计算距离
	# [2]      [A]
	# [1.41]   [B]
	# [4]      [C]
	# step2: 排序距离
	# [1.41]   [B]
	# [2]      [A]
	# [4]      [C]
	# step3: 返回标签
	# k为2时,返回 [B, A]

	row = dataSet.shape[0]  # 行数
	diff = tile(newInput, (row, 1)) - dataSet
	# tile(A, (r, c)) ==> 将A的行复制r次, 列复制c次
	#                           [[1, 2, 1, 2],
	# [[1, 2],  tile(A, (2, 2))  [3, 4, 3, 4],
	#  [3, 4]]      ===>         [1, 2, 1, 2],
	#							 [3, 4, 3, 4]]
	diffSquared = diff ** 2
	sumSquared = sum(diffSquared, axis=1)
	distance = sumSquared ** 0.5
	sortedDiff = argsort(distance)  # 返回排名(以1开始),距离越小,排名越小
	
	classCount = {}
	# 选取k个近邻
	for i in range(k):
		lab = labels[sortedDiff[i]] 
		classCount[lab] = classCount.get(lab, 0) + 1

	# 返回出现次数最多的类别标签
	print(classCount)
	print(distance)
	# key = operator.itemgetter(1) 获取第一个值
	maxLabel = sorted(classCount.items(), key=lambda x: x[1], reverse=True)[0][0]
	
	return maxLabel


##############################################
# 测试
##############################################

# dataSet, labels = createDataSet()
# newInput = array([1.5, 0.8])
# k = 3
# output = knnClassify(newInput, dataSet, labels, k)
# print('Input: ', newInput, '  Output: ', output)

# newInput = array([0.3, 0.5])
# k = 3
# output = knnClassify(newInput, dataSet, labels, k)
# print('Input: ', newInput, '  Output: ', output)


#######################################################

def file2matric(filename):
	fn = open(filename, mode='r', encoding='utf-8')
	lines = fn.readlines()
	# print(lines)
	random.shuffle(lines)
	rows = len(lines)
	matr = np.zeros((rows, 3))
	labels = []
	index = 0      # 行索引 
	for line in lines:
		line_list = line.strip().split('\t')
		matr[index, :] = line_list[:3]
		if line_list[-1] == 'didntLike':
			labels.append(1)
		elif line_list[-1] == 'smallDoses':
			labels.append(2)
		else:
			labels.append(3)
		index += 1

	return matr, labels

##############################################################

def showDatas(dataMat, dataLabels):
	font = FontProperties(fname='/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc', size=12)
	fig, axs = plt.subplots(nrows=2, ncols=2, sharex=False, sharey=False, figsize=(13, 8))

	nlabels = len(dataLabels)
	labelColors = []
	for i in dataLabels:
		if i == 1:
			labelColors.append('black')
		if i == 2:
			labelColors.append('orange')
		if i == 3:
			labelColors.append('red')
	axs[0][0].scatter(x=dataMat[:, 0], y=dataMat[:, 1], color=labelColors, s=10, alpha=0.5)
	axs0_title_text = axs[0][0].set_title('每年获得的飞行里程数与玩视频游戏消耗时间占比',
										FontProperties=font)
	axs0_xlabel_text = axs[0][0].set_xlabel('每年获得的飞行常客里程数',
										FontProperties=font)
	axs0_ylabel_text = axs[0][0].set_ylabel('玩游戏消耗的时间',
										FontProperties=font)
	plt.setp(axs0_title_text, size=13, weight='bold', color='red')


	axs[0][1].scatter(x=dataMat[:, 0], y=dataMat[:, 2], color=labelColors, s=10, alpha=0.5)
	axs0_title_text = axs[0][1].set_title('每年获得的飞行里程数与冰激淋公斤数占比',
										FontProperties=font)
	axs0_xlabel_text = axs[0][1].set_xlabel('每年获得的飞行常客里程数',
										FontProperties=font)
	axs0_ylabel_text = axs[0][1].set_ylabel('冰激淋公斤数',
										FontProperties=font)
	plt.setp(axs0_title_text, size=13, weight='bold', color='red')


	axs[1][0].scatter(x=dataMat[:, 1], y=dataMat[:, 2], color=labelColors, s=10, alpha=0.5)
	axs0_title_text = axs[1][0].set_title('玩游戏消耗的时间与冰激淋公斤数占比',
										FontProperties=font)
	axs0_xlabel_text = axs[1][0].set_xlabel('玩游戏消耗的时间',
										FontProperties=font)
	axs0_ylabel_text = axs[1][0].set_ylabel('冰激淋公斤数',
										FontProperties=font)
	plt.setp(axs0_title_text, size=13, weight='bold', color='red')

	# 设置图例
	didntLike = mines.Line2D([], [], color='black', marker='.', markersize=6, label='didntLike')
	smallDose = mines.Line2D([], [], color='orange', marker='.', markersize=6, label='smallDose')
	largeDose = mines.Line2D([], [], color='red', marker='.', markersize=6, label='largeDose')
	
	# 添加图例
	axs[0][0].legend(handles=[didntLike, smallDose, largeDose])
	axs[0][1].legend(handles=[didntLike, smallDose, largeDose])
	axs[1][0].legend(handles=[didntLike, smallDose, largeDose])

	# plt.subplots_adjust(hspace=0.35, wspace=0.35)
	plt.subplots_adjust(hspace=0.35)
	plt.show()


# if __name__ == '__main__':
# 	filename = './action/Ch02/datingTestSet.txt'
# 	mat, labels = file2matric(filename)
# 	showDatas(mat, labels)

#################################################

def autoNorm(dataSet):
	'''
	dataSet: numpy格式 
	'''
	print('*' * 20)
	minVal = dataSet.min(0) # 0 - 表示纵轴上的  1 - 表示横轴	
	maxVal = dataSet.max(0)	
	print(minVal, maxVal)
	ranges = maxVal - minVal

	normDataSet = np.zeros(np.shape(dataSet))
	m = dataSet.shape[0]
	normDataSet = dataSet - np.tile(minVal,(m, 1))
	normDataSet = normDataSet / np.tile(ranges, (m, 1))

	return normDataSet, ranges, minVal


##############################################################

def classify(inX, dataSet, labels, k):
	'''
	inX: 		待分类集
	dataSet: 	训练集
	labels: 	分类标签
	k: 			最近的k个点
	return:		分类结果
	'''
	rows = dataSet.shape[0]
	diffMat = np.tile(inX, (rows, 1)) - dataSet
	sqDiffMat = diffMat ** 2
	sqDistances = sqDiffMat.sum(axis=1)
	distances = sqDistances ** 0.5
	sortedDistances = distances.argsort()
	classCount = {}
	for i in range(k):
		voteLabel = labels[sortedDistances[i]]
		classCount[voteLabel] = classCount.get(voteLabel, 0) + 1
	sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
	return sortedClassCount[0][0]


def datingClassTest():
	filename = './action/Ch02/datingTestSet.txt'
	dataMat, labels = file2matric(filename)
	# dataMat = random.shuffle(dataMat)
	hoRatio = 0.1
	normMat, ranges, minVal = autoNorm(dataMat)
	m = normMat.shape[0]
	print('数据个数: %d' % m)
	numTestVecs = int(m*hoRatio)
	errorCount = 0.0

	for i in range(numTestVecs):
		classifierResult = classify(normMat[i, :], normMat[numTestVecs:m, :],
			labels[numTestVecs:m], 10)
		print('分类结果: %d\t 真实类别: %d' % (classifierResult, labels[i]))
		if classifierResult != labels[i]:
			errorCount += 1.0
	print('错误率: %.2f%%' % (errorCount / numTestVecs * 100))


if __name__ == '__main__':
	datingClassTest()