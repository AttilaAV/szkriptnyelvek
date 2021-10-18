from median import median

def test_median():
	assert median([3,6,20,99,10,15]) == 12.5
	assert median([1, 2, 3, 4, 6]) == 3