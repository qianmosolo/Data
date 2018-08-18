# coding: utf-8

import codecs
from math import sqrt

users = {"Angelica": {"Blues Traveler": 3.5, "Broken Bells": 2.0, "Norah Jones": 4.5, "Phoenix": 5.0, "Slightly Stoopid": 1.5, "The Strokes": 2.5, "Vampire Weekend": 2.0},
         "Bill":{"Blues Traveler": 2.0, "Broken Bells": 3.5, "Deadmau5": 4.0, "Phoenix": 2.0, "Slightly Stoopid": 3.5, "Vampire Weekend": 3.0},
         "Chan": {"Blues Traveler": 5.0, "Broken Bells": 1.0, "Deadmau5": 1.0, "Norah Jones": 3.0, "Phoenix": 5, "Slightly Stoopid": 1.0},
         "Dan": {"Blues Traveler": 3.0, "Broken Bells": 4.0, "Deadmau5": 4.5, "Phoenix": 3.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 2.0},
         "Hailey": {"Broken Bells": 4.0, "Deadmau5": 1.0, "Norah Jones": 4.0, "The Strokes": 4.0, "Vampire Weekend": 1.0},
         "Jordyn":  {"Broken Bells": 4.5, "Deadmau5": 4.0, "Norah Jones": 5.0, "Phoenix": 5.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 4.0},
         "Sam": {"Blues Traveler": 5.0, "Broken Bells": 2.0, "Norah Jones": 3.0, "Phoenix": 5.0, "Slightly Stoopid": 4.0, "The Strokes": 5.0},
         "Veronica": {"Blues Traveler": 3.0, "Norah Jones": 5.0, "Phoenix": 4.0, "Slightly Stoopid": 2.5, "The Strokes": 3.0}
        }


def manhattan(rating1, rating2):
	'''计算曼哈顿距离'''
	distance = 0
	for key in rating1:
		if key in rating2:
			distance += abs(rating2[key] - rating1[key])
	return distance

# print manhattan(users['Sam'], users['Veronica'])

def computerNearestNeighbor(username, users, func=manhattan):
	'''
	寻找距离最近的用户
	func为计算距离方法
	'''
	distances = []
	# if username not in users:
	# 	raise KeyError(username + ' does not exist')
	for user in users:
		if username != user:
			distance = func(users[user], users[username])
			distances.append((distance, user))
	distances.sort()
	return distances

# print computerNearestNeighbor('Chan', users, manhattan)

def recommend(username, users):
	'''推荐'''
	nearest = computerNearestNeighbor(username, users)[0][1]
	recommendations = []
	otherItems = users[nearest]
	userItems = users[username]

	for item in otherItems:
		if item not in userItems:
			recommendations.append((item, otherItems[item]))

	return sorted(recommendations, key=lambda x: x[1], reverse=True)

# print recommend('Chan', users)


def minkowski(rating1, rating2, r=2):
	# r=2 表示欧几里得(勾股)距离
	distance = 0
	for key in rating1:
		if key in rating2:
			distance += pow(abs(rating1[key] - rating2[key]), r)
	return pow(distance, 1.0 / r)

# print minkowski(users['Sam'], users['Veronica'])
# print computerNearestNeighbor('Chan', users, minkowski)


def pearson(rating1, rating2):
	'''
	皮尔逊
	'''
	sum_xy = 0
	sum_x, sum_y = 0, 0
	sum_x2, sum_y2 = 0, 0
	n = 0
	for key in rating1:
		if key in rating2:
			n += 1
			x = rating1[key] 
			y = rating2[key] 
			sum_xy += x * y
			sum_x += x
			sum_y += y
			sum_x2 += pow(x, 2)
			sum_y2 += pow(y, 2)
	# 分母
	denominator = sqrt(sum_x2 - pow(sum_x, 2) / n) * sqrt(sum_y2 - pow(sum_y, 2) / n)
	if denominator == 0:
		return 0
	else:
		return (sum_xy - (sum_x * sum_y) / n) / denominator

# print pearson(users['Sam'], users['Veronica'])


def cosineSimilarity(rating1, rating2):
	'''余弦相似度'''
	x, y, xy = 0, 0, 0
	
	for key in rating1:
		if key in rating2:
			x += pow(rating1[key], 2)
			y += pow(rating2[key], 2)
			xy += rating1[key] * rating2[key]
	return xy / (sqrt(x) * sqrt(y))

# Clara = {'Blues Traveler': 4.75, 'Norah Jones': 4.5, 'Phoenix': 5, 'The Strokes': 4.25, 'Weird Al': 4}
# Robert = {'Blues Traveler': 4, 'Norah Jones': 3, 'Phoenix': 5, 'The Strokes': 2, 'Weird Al': 1}

# print cosineSimilarity(users['Veronica'], users['Angelica'])
# print cosineSimilarity(Clara, Robert)


class recommender:
	def __init__(self, data, k=1, method='pearson', n=5):
		self.k = k
		self.n = n
		self.method = method
		self.productid2name = {}
		self.userid2name = {}
		self.username2id = {}


		if isinstance(data, dict):
			self.data = data


	def loadData(self, path=''):
		self.data = {}
		i = 0
		f = codecs.open(path + 'BX-Book-Ratings.csv', 'r', 'utf8')
		for line in f:
			i += 1
			fields = line.split(';')
			userid = fields[0].strip('"')
			bookid = fields[1].strip('"')
			rating = int(fields[2].strip().strip('"'))
			if userid in self.data:
				currentRatings = self.data[userid]
			else:
				currentRatings = {}
			currentRatings[bookid] = rating
			self.data[userid] = currentRatings
		f.close()

		f = codecs.open(path + 'BX-Books.csv', 'r', 'utf8')
		for line in f:
			i += 1
			fields = line.split(';')
			isbn = fields[0].strip('"')
			title = fields[1].strip('"')
			author = fields[2].strip('"').strip()
			title = title + ' by ' + author
			self.productid2name[isbn] = title
		f.close()

		f = codecs.open(path + 'BX-Users.csv', 'r', 'utf8')
		for line in f:
			i += 1
			fields = line.split(';')
			userid = fields[0].strip('"')
			location = fields[1].strip('"')
			if len(fields) > 2:
				age = fields[2].strip().strip('"')
			else:
				age = 'NULL'
			if age != 'NULL':
				value = location + ' (age: ' + age + ')'
			else:
				value = location
			self.userid2name[userid] = value
			self.username2id[location] = userid
		f.close()
		print(i)

	def getProductNameById(self, id):
		return self.productid2name.get(id, id)

	def userRatings(self, id, n):
		print 'Ratings for ' + self.userid2name[id]
		ratings = self.data[id]
		print len(ratings)
		ratings = list(ratings.items)
		ratings = [(self.getProductNameById(k), v)
					for (k, v) in ratings]
		ratings.sort(key=lambda x: x[1], reverse=True)

		ratings = ratings[:n]
		for rating in ratings:
			print '%s\t%i' % (rating[0], rating[1])

	
	def pearson(self, rating1, rating2):
		'''
		皮尔逊
		'''
		sum_xy = 0
		sum_x, sum_y = 0, 0
		sum_x2, sum_y2 = 0, 0
		n = 0
		for key in rating1:
			if key in rating2:
				n += 1
				x = rating1[key] 
				y = rating2[key] 
				sum_xy += x * y
				sum_x += x
				sum_y += y
				sum_x2 += pow(x, 2)
				sum_y2 += pow(y, 2)
		if n == 0:
			return 0 
		# 分母
		denominator = sqrt(sum_x2 - pow(sum_x, 2) / n) * sqrt(sum_y2 - pow(sum_y, 2) / n)
		if denominator == 0:
			return 0
		else:
			return (sum_xy - (sum_x * sum_y) / n) / denominator


	def computerNearestNeighbor(self, username):
		'''
		寻找距离最近的用户
		'''
		distances = []
		# if username not in users:
		# 	raise KeyError(username + ' does not exist')
		for user in self.data:
			if user != username:
				distance = self.pearson(self.data[username], self.data[user])
				distances.append((user, distance))
		# pearson相关系数越大,越相似
		distances.sort(key=lambda x: x[1], reverse=True)
		return distances

	# print computerNearestNeighbor('Chan', users, manhattan)

	def recommend(self, user):
		'''推荐'''
		nearest = self.computerNearestNeighbor(user)
		recommendations = {}

		userItems = self.data[user]

		totalDistance = 0.0
		for i in range(self.k):
			totalDistance += nearest[i][1]

		for i in range(self.k):
			weight = nearest[i][1] / totalDistance
			name = nearest[i][0]
			neighborItems = self.data[name]
			for artist in neighborItems:
				if artist not in userItems:
					if artist not in recommendations:
						recommendations[artist] = (neighborItems[artist] * weight)
					else:
						recommendations[artist] = (neighborItems[artist] + 
													neighborItems[artist] * weight)
		
		recommendations = list(recommendations.items())
		recommendations = [(self.getProductNameById(k), v)
							for (k, v) in recommendations]
		recommendations.sort(key=lambda x: x[1], reverse=True)
		
		return recommendations[:self.n]



r = recommender(users)
# print r.recommend('Jordyn')
# print r.recommend('Hailey')

r.loadData('./BX-Dump/')
print r.recommend(u'171118')