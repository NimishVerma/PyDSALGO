class TrieNode:
	def __init__(self):

		self.children = {}
		self.end = False


def getIndex(letter):
	return ord(letter) - ord('a')

def constructTrie(wordList):
	root = TrieNode()
	global orignal_root
	orignal_root = root
	for word in wordList:
		for letter in word:
			if getIndex(letter) not in root.children:
			    root.children[getIndex(letter)] = TrieNode()

			root = root.children[getIndex(letter)]
		root.end = True
		root = orignal_root

	return orignal_root

a = constructTrie(['cat','can','cans'])

# print (a.children[2].children[0].children[13].__dict__)

def inv_index(index):
	return chr(97+index)

def searchRec(node,word, results):
    if node.end == True:
    	results.append(word)
    for index, n in node.children.items():

        searchRec(n, word+inv_index(index), results)
def searchInTrie(root, word):
	for letter in word:
		if getIndex(letter) not in root.children:
			return -1
		root = root.children[getIndex(letter)]
	results = []
	searchRec(root, word, results)
 			
	return results

print(searchInTrie(a,'can'))

