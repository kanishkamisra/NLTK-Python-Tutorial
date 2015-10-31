# This shit doesn't make sense but oh well. Experiment has ben experimented.

from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize as wt

ps = PorterStemmer()

# words = ["python", "pythoner", "pythoning", "pythoned", "pythonly"]

# for w in words:
# 	print ps.stem(w)

new_text = "It is very important to be pythonly while you are pythoning with python. All pythoners have pythoned poorly at least once"
words = wt(new_text)

for w in words:
	print ps.stem(w)