# Project:		Clockwork Wars Cleanup
# Description:	A greedy sort to simulate the tile cleanup for the Clockwork Wars board game.
# Input:		A randomized list of alphanumeric values.
# Output:		A matrix of alphanumeric values sorted by.
# Creator:		Dana Oira Toribio
# Duration:		8/6/2016 - 8/7/2016

# Outline:
	# Value generation
		# Values: V1-V7, C1-C7, L1-L7, F1-F7, T1-T7, M1-M7, S1-S7
		# RegEx: [(C|F|L|M|S|T|V)(1-7)]
	# Randomize values
	# Place values into matrix
	# Print results to file

import random

f = open('results.txt', 'w')
alpha = ['C', 'F', 'L', 'M', 'S', 'T', 'V']
num = 7	# max int value (see outline above)

def create_items(alpha):
	items = []
	for i in alpha:
		for j in range(1, num + 1):	# range = 1-7
			val = i + str(j)	# => 'C1', 'C2', etc
			items.append(val)
	random.shuffle(items)
	return items

def create_matrix(col, row):
	return [['  ' for x in range(col)] for y in range(row)]

def write_result(val, is_matrix):
	if is_matrix == False:
		f.write(str(val))
	elif is_matrix == True:	
		for i in val:
			f.write('\n' + str(i))

def update_result(items):
	for i in items:			# ex. i = C2
		f.write('\n\nRound ' + str(items.index(i) + 1) + ' (' + str(i) + ')\n')
		result[int(i[1]) - 1][alpha.index(i[0])] = i
		write_result(result, True)

print('Running Clockworks Wars Cleanup')

print('... created randomized list')
items = create_items(alpha)
write_result(items, False)

print('... created matrix')
result = create_matrix(len(alpha), num)	# => create_matrix(7, 7)

print('... updated result')
update_result(items)

print('... completed result for ' + str(len(items)) + ' items')