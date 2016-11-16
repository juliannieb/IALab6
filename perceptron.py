import sys
from random import choice
from numpy import array, dot, random
from random import randint

def get_random_position(data):
	n = len(data)
	return data[randint(0, n - 1)]

def unit_step(x):
    if x < 0:
        return 0
    else:
        return 1

training_data = []

for line in sys.stdin:
    line = line.strip("\n")
    line = line.split(' ')
    data = (array([int(i) for i in line[:len(line)-1]]), int(line[len(line)-1]))
    training_data.append(data)

print(training_data)

w = random.rand(3)
eta = 0.2
n = 100

for i in xrange(n):
    x, expected = get_random_position(training_data)
    result = dot(w, x)
    error = expected - unit_step(result)
    w += eta * error * x

for x, _ in training_data:
    result = dot(x, w)
    print("{}: {} -> {}".format(x[:2], result, unit_step(result)))