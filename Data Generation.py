import random
import matplotlib.pyplot as plt


class test():
	def __init__(self, powersArray, error):
		self.powers = powersArray
		self.error = error


class results():
	def __init__(self, formula, error, size):
		# is the original formula of the line that created the data
		self.original = formula
		# is the paramaters such as how many data points and how much error
		self.params = {"error": error, "size": size}


class dataset():
	def __init__(self, error, numberOfDataPoints, xFive, xFour, xThree, xTwo, xOne, xZero):
		# an array of all of the tupples of (x,y)
		self.dataTup = []
		# splitting up the data into x and y arrays for display
		self._coords = {"x": [], "y": []}
		# a meta class that holds the formula, error and number of data points
		self.meta = results({"xFive" : int(xFive),
							 "xFour" : int(xFour),
							 "xThree": int(xThree),
							 "xTwo"  : int(xTwo),
							 "xOne"  : int(xOne),
							 "xZero" : int(xZero)},
							int(error),
							numberOfDataPoints)
		self._data_generation()
		self.zeroError = []
		print(self.test_Zero(71, 43, 232, 0, 45).powers)

	def _data_generation(self):
		for i in range(self.meta.params["size"]):
			x = random.randint(-100, 100)
			self.dataTup.append((x, (
					self.meta.original["xFive"] * (x ** 5)) + (
										 self.meta.original["xFour"] * (x ** 4)) + (
										 self.meta.original["xThree"] * (x ** 3)) + (
										 self.meta.original["xTwo"] * (x ** 2)) + (
										 self.meta.original["xOne"] * (x ** 1)) + (
										 self.meta.original["xZero"] * (x ** 0)) + (
									 random.randint(-self.meta.params["error"], self.meta.params["error"]))))

	def _data_split(self):
		for coords in self.dataTup:
			self._coords["x"].append(coords[0])
			self._coords["y"].append(coords[1])

	def _data_spliterror(self):
		self._coords["x"] = []
		self._coords["y"] = []
		for coords in self.zeroError:
			self._coords["x"].append(coords[0])
			self._coords["y"].append(coords[1])

	def display(self):
		if len(self._coords["x"]) != len(self.dataTup) and len(self._coords["y"]) != len(self.dataTup):
			self._data_split()
		fig, ax = plt.subplots(figsize=(10, 5))
		ax.scatter(self._coords["x"], self._coords["y"])
		plt.xlabel('x - axis')
		plt.ylabel('y - axis')
		plt.show()

	def displayError(self):
		self._data_spliterror()
		fig, ax = plt.subplots(figsize=(10, 5))
		ax.scatter(self._coords["x"], self._coords["y"])
		plt.xlabel('x - axis')
		plt.ylabel('y - axis')
		plt.show()

	def compareError(self, five, four, three, two, one, zero):
		error = []
		for xy in self.dataTup:
			error.append(abs(
				((five * (xy[0] ** 5)) + (
						four * (xy[0] ** 4)) + (
						 three * (xy[0] ** 3)) + (
						 two * (xy[0] ** 2)) + (
						 one * (xy[0] ** 1)) + (
						 zero * (xy[0] ** 0))) - xy[1]))
		return float(sum(error)) / float(len(error))

	# runs all tests
	def test(self):
		pass

	# runs tests for x^5 and all sub powers
	def test_Five(self):
		pass

	# runs tests for x^4 and all sub powers
	def test_Four(self, five):
		pass

	# runs tests for x^3 and all sub powers
	def test_Three(self, five, four):
		pass

	# runs tests for x^2 and all sub powers
	def test_Two(self, five, four, three):
		pass

	# runs tests for x^1 and all sub powers
	def test_One(self, five, four, three, two):
		pass

	# runs tests for x^0 and all sub powers
	def test_Zero(self, five, four, three, two, one, startVal=0, searchArea=100):
		high = self.compareError(five, four, three, two, one, startVal + searchArea)
		self.zeroError.append((startVal + searchArea, high))
		mid = self.compareError(five, four, three, two, one, startVal)
		self.zeroError.append((startVal, mid))
		low = self.compareError(five, four, three, two, one, startVal - searchArea)
		self.zeroError.append((startVal - searchArea, low))
		# print(high, mid, low, five, four, three, two, one, startVal, searchArea)
		# print(self.zeroError)
		if mid == 0:
			return test([five, four, three, two, one, startVal], mid)
		elif high == 0:
			return test([five, four, three, two, one, startVal - searchArea], high)
		elif low == 0:
			return test([five, four, three, two, one, startVal + searchArea], low)
		elif mid <= high and mid <= low:
			if searchArea > 1:
				return self.test_Zero(five, four, three, two, one, startVal, int(searchArea / 1.5))
			else:
				return test([five, four, three, two, one, startVal], mid)
		elif low <= mid and low <= high:
			return self.test_Zero(five, four, three, two, one, int(startVal - searchArea), searchArea)
		elif high <= mid and high <= low:
			return self.test_Zero(five, four, three, two, one, int(startVal + searchArea), searchArea)


"""
largeDataTest = []
for i in range(10):
	largeDataTest.append(dataset(0,
								 20,
								 random.randint(-10, 10),
								 random.randint(-10, 10),
								 random.randint(-10, 10),
								 random.randint(-10, 10),
								 random.randint(-10, 10),
								 random.randint(-10, 10)))
for i in largeDataTest:
	print(i.meta.original)
# data1.display()
"""

data = dataset(0, 20, 71, 43, 232, 0, 45, 120)
data.display()
data.displayError()
