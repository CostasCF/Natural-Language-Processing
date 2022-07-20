from FileOperations import FileOperations
from Tokenizer import Tokenizer

# Create objects of the classes we created
tok = Tokenizer()
fileOperations = FileOperations()

# Initialize sentence list: ex. ['sentence A', 'sentence B', ...]
file = str(input("Enter the file for Semantic Analysis: "))
sentences_list = tok.tokenizeSentences(fileOperations.readFromFile(file))

# Initialize words list: ex. [['word A1', 'word A2'], [word B1], [word B2], ...]
fileOperations.writeToFile(tok.tokenize_words(sentences_list))
file = fileOperations.readFromFile("tokenized_text.txt")
fileOperations.printFile(file)