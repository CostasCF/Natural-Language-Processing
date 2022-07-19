
from FileOperations import FileOperations
from Tokenizer import Tokenizer

# Create objects of the classes we created
tok = Tokenizer()
fileOperations = FileOperations()

# Initialize sentence list: ex. ['sentence A', 'sentence B', ...]
sentences_list = tok.tokenizeSentences(fileOperations.readFromFile())

# Initialize words list: ex. [['word A1', 'word A2'], [word B1], [word B2], ...]
fileOperations.writeToFile(tok.tokenize_words(sentences_list))