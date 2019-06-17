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
