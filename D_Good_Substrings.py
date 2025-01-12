string = input()
permission = input()
k = int(input())

class TrieNode:

    def __init__(self):
        self.letters = [None for _ in range(26)]
        self.badLetters = 0
        self.isEnd = False

class Trie:

    def __init__(self):

        self.root = TrieNode()
        self.words = []

    def addWord(self, word, badOnes):

        curr = self.root
        for char in word:
            if not curr.letters[ord(char) - ord('a')]:
                curr.letters[ord(char) - ord('a')] = TrieNode()
            curr = curr.letters[ord(char) - ord('a')]
            curr.isEnd = True

    def getWords(self, string, node):

        for i in range(26):
            if node.letters[i]:
                word = string + chr(ord('a') + i)
                if node.letters[i].isEnd:
                    self.words.append(word)
                    self.getWords(word, node.letters[i])

        return self.words

def countBad(word, k = k):

    count = 0
    for char in word:
        if permission[ord(char) - ord('a')] == '0':
            count += 1
    return count

dictionary = Trie()
for i in range(len(string)):
    word = string[i:]
    badOnes = countBad(word)
    dictionary.addWord(word, badOnes)


words = dictionary.getWords('', dictionary.root)
result = 0
for word in words:
    if countBad(word):
        result += 1

print(result)
