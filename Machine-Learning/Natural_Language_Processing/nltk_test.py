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

#Example of stem

from nltk.stem import PorterStemmer

ps=PorterStemmer()

example_verbs=["ride","riding","jump","jumping","swimming","swim","eat","eating","ate"]

words=word_tokenize(example)

for w in words:
    print(ps.stem(w))
    
for v in example_verbs:
    print(ps.stem(v))