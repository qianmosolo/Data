# coding: utf-8

from numpy import *
import operator


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
	maxLabel = sorted(classCount.items(), key=lambda x: x[1], reverse=True)[0][0]
	
	return maxLabel


##############################################
# 测试
##############################################

dataSet, labels = createDataSet()
newInput = array([1.5, 0.8])
k = 3
output = knnClassify(newInput, dataSet, labels, k)
print('Input: ', newInput, '  Output: ', output)

newInput = array([0.3, 0.5])
k = 3
output = knnClassify(newInput, dataSet, labels, k)
print('Input: ', newInput, '  Output: ', output)