from nltk.data import load
from TreeCalculations import TreeCalculations

#loading grammar
grammar = load("file:grammar.cfg")

input_sentence = ['the', 'dog', 'chased', 'the', 'cat']

treeCalculations = TreeCalculations()

#calculate tree
tree = treeCalculations.calculateTree(grammar,input_sentence)
#print tree in console
treeCalculations.printTree(tree)
#create tree's image to PNG
treeCalculations.createTreeImage(tree)
