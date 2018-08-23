# coding: utf-8

import operator
from math import log

def calcShannonEnt(dataSet):
	numEntries = len(dataSet)
	labelCounts = {}
	for featVec in dataSet:
		label = featVec[-1]
		if label not in labelCounts.keys():
			labelCounts[label] = 0
		labelCounts[label] += 1
	
	shannoEnt = 0.0
	for key in labelCounts:
		prob = float(labelCounts[key]) / numEntries
		shannoEnt -= prob * log(prob, 2)
	return shannoEnt

def createDataSet():
	'''
	['不浮出水面是否可以生存', '是否有鳍', '是否为鱼类(结论)']
	'''
	dataSet = [[1, 1, 'yes'],			
			[1, 1, 'yes'],
			[1, 0, 'no'],
			[0, 1, 'no'],
			[0, 1, 'no'],
			[1, 1, 'maybe'],
			[1, 1, 'yes'],
			[1, 0, 'no'],
			[0, 1, 'no']]
	labels = ['no surfacing', 'flippers']
	return dataSet, labels

datas, labels = createDataSet() 
# print(calcShannonEnt(datas))


def splitDataSet(dataSet, axis, value):				# axis=0, value=1
	''''''
	retDataSet = []
	for featVec in dataSet:							# [1, 1, 'yes']
		if featVec[axis] == value:					# axis: 列数	 value: 类别
			reducedFeatVec = featVec[:axis]			# []
			reducedFeatVec.extend(featVec[axis+1:]) # [第1列, ...] 
			retDataSet.append(reducedFeatVec)		# [[第1列, ...], [第1列, ...], ...]
	return retDataSet

# print(splitDataSet(datas, 0, 1))
# print(splitDataSet(datas, 0, 0))

def chooseBestFeatureTopSplit(dataSet):
	numFeatures = len(dataSet[0]) - 1			# 有一列为结论, 减少一列
	baseEntropy = calcShannonEnt(dataSet)		# 计算所有数据的香农熵
	bestInfoGain = 0.0
	bestFeature = -1							# 初始化 最好的特征值
	for i in range(numFeatures):				# 列循环
		featList = [example[i] for example in dataSet] # 取某一列的所有值
		uniqueVals = set(featList)				# 去重, 得到此列所有特征
		newEntropy = 0.0						 
		for value in uniqueVals:				# 特征循环
			subDataSet = splitDataSet(dataSet, i, value)	# 返回具有某一特征值的数据集 
			prob = len(subDataSet) / float(len(dataSet))    # 计算百分比(概率)
			newEntropy += prob * calcShannonEnt(subDataSet)	# 累加此列不同特征的香农熵
		infoGain = baseEntropy - newEntropy					# 计算此列的信息增量
		if infoGain > bestInfoGain:							# 获取最最大的信息增量及列数
			bestInfoGain = infoGain
			bestFeature = i
	return bestFeature 		# 返回影响数据纯度的类别(列)

# print(chooseBestFeatureTopSplit(datas))


def mainjorCnt(classList):
	'''投票选择类别'''
	classCount = {}
	for vote in classList:
		if vote not in classCount.keys():
			classCount[vote] = 0
		classCount[vote] += 1
	sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
	return sortedClassCount[0][0]


def createTree(dataSet, labels):
	classList = [example[-1] for example in dataSet]	 # 统计类别
	if classList.count(classList[0]) == len(classList):	 # 只有一个类别
		return classList[0]
	if len(dataSet[0]) == 1:		 # 如果训练集中只有一列数据, 通过投票分类
		return mainjorCnt(classList)
	bestFeat = chooseBestFeatureTopSplit(dataSet) # 选取最好的特征值列: 0或者其他整数
	bestFeatLabel = labels[bestFeat] # 返回特征值对应的标签
	myTree = {bestFeatLabel: {}}	# {'no surfacing': {}}
	del(labels[bestFeat])
	featValues = [example[bestFeat] for example in dataSet] # 所有特征值列的数据
	uniqueVals = set(featValues)	# 去重 (0, 1)
	for value in uniqueVals:
		subLabels = labels[:]		# ['no surfacing', 'flippers']
		myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet, 
										bestFeat, value), subLabels)    # {'no surfacing': {'0': ..., '1': }}
	return myTree

print(createTree(datas, labels))