# coding: utf-8

from math import sqrt

users = {"David": {"Imagine Dragons": 3, "Daft Punk": 5,
                    "Lorde": 4, "Fall Out Boy": 1},
          "Matt": {"Imagine Dragons": 3, "Daft Punk": 4,
                   "Lorde": 4, "Fall Out Boy": 1},
          "Ben": {"Kacey Musgraves": 4, "Imagine Dragons": 3,
                  "Lorde": 3, "Fall Out Boy": 1},
          "Chris": {"Kacey Musgraves": 4, "Imagine Dragons": 4,
                    "Daft Punk": 4, "Lorde": 3, "Fall Out Boy": 1},
          "Tori": {"Kacey Musgraves": 5, "Imagine Dragons": 4,
                   "Daft Punk": 5, "Fall Out Boy": 3}
}

def similarity(band1, band2, users):
	'''
	修正的余弦相似度
	'''
	averages = {}
	for (key, ratings) in users.items():
		averages[key] = float(sum(ratings.values()) / len(ratings.values()))

	num = 0
	dem1 = 0
	dem2 = 0
	for (key, ratings) in users.items():
		if band1 in ratings and band2 in ratings:
			avg = averages[key]
			num += (ratings[band1] - avg) * (ratings[band2] - avg)
			dem1 += (ratings[band1] - avg) ** 2 
			dem2 += (ratings[band2] - avg) ** 2 
	return num / (sqrt(dem1) * sqrt(dem2))

print similarity('Kacey Musgraves', 'Lorde', users)
print similarity('Imagine Dragons', 'Lorde', users)
print similarity('Daft Punk', 'Lorde', users)
