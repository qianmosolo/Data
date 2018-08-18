# coding: utf-8

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
