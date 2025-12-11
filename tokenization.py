import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize

text = "This is example for tokenization using nltk"
tokens = word_tokenize(text)
print(tokens)
