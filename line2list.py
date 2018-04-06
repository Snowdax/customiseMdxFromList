import re

lineFileName = input('Please input wordlist (each word a line) filename (without .txt).\n> ')

lineRegex = re.compile(r'''(
		(.{1,})
		)''', re.VERBOSE)

fo = open('%s.txt' % lineFileName)
data = fo.read()
fo.close()

matches = []
for groups in lineRegex.findall(data):
	word = groups[1]
	matches.append(word)

fo = open('%s_list.py' % lineFileName, 'w')
data = 'wordList = ' + str(matches)
fo.write(data)
fo.close
