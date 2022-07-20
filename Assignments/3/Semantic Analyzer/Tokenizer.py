from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
class Tokenizer():

    # Creare list of the sentances of the given text
    def tokenizeSentences(self, raw_text: str):
        sentences = sent_tokenize(raw_text)

        return sentences

    # Create list of words from a given list of sentences and tag each word.
    def tokenize_words(self, sentence_list: list):
        words = []
 
        for sentence in sentence_list:
            words_of_sentece = pos_tag(word_tokenize(sentence),tagset="universal")
            words.append(words_of_sentece)

        return words