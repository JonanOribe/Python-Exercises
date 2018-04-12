from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example="This is just a basics example of how you can use the stop word filter during your work with nltk"
stop_words=set(stopwords.words("english"))

words=word_tokenize(example)

sentence_with_filter=[]

for w in words:
    if w not in stop_words:
        sentence_with_filter.append(w)
        
print(sentence_with_filter)