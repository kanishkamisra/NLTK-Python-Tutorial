from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize as wt
from nltk.tokenize import sent_tokenize as st

example_sentence = "This is an example showing off stop word filteration"
example_sentences = "This is an example showing off stop word filteration. this is another sentence which shows how stop words filteration is used. How are you"
stop_words = set(stopwords.words("english"))
 # print stop_words

words = wt(example_sentence)
sentences = st(example_sentences)
filtered_sentence = [ w for w in words if w not in stop_words]
more_words = [wt(s) for s in sentences]

for mw in more_words:
	more_filtered_sentences = [m for m in mw if m not in stop_words]

print filtered_sentence
print more_filtered_sentences
