f = open("pulpfiction.txt", "r")

# print out adverbs in pulp fiction's script
# (warning: not all are adverbs)
for line in f:
	line = line.split()
	for word in line:
		if word[-2:] == 'ly':
			print word
		
