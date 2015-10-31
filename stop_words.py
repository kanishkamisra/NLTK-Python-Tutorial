from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize as wt

example_sentence = "This is an example showing off stop word filteration"
stop_words = set(stopwords.words("english"))
 # print stop_words

words = wt(example_sentence)
filtered_sentence = [ w for w in words if w not in stop_words]

print filtered_sentence