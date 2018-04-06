import re, time
import COCA5000_list
# wordlist .py filename (without .py)

mdxTxtFileName = input('Please input mdx .txt filename (without .txt).\n> ')

startTime = time.time()

fo = open('%s.txt' % mdxTxtFileName, encoding='UTF-8')
data = fo.read()
data = '\n' + data
fo.close()

matches = []
for i in COCA5000_list.wordList:
	mdxRegex = re.compile(r'''(
			\n{1}
			(%s){1}
			(\n){1}
			(.*)
			(\n){1}
			(</>){1}
			)''' % i, re.VERBOSE)

	for groups in mdxRegex.findall(data):
		word = groups[1] + groups[2] + groups[3] + groups[4] + groups[5]
		matches.append(word)

fo = open('%s_customised.txt' % mdxTxtFileName, 'w', encoding='UTF-8')
data = '\n'.join(matches)
fo.write(data)
fo.close()

print('Time consumed: ' + str(round((time.time() - startTime), 2)) + 's')