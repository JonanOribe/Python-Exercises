import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

train_text=state_union.raw("2006-GWBush.txt")
sample=state_union.raw("2004-GWBush.txt")

custom_sent=PunktSentenceTokenizer(train_text)
tokenized=custom_sent.tokenize(sample)

def process_i():
    try:
        for i in tokenized:
            words=nltk.word_tokenize(i)
            tagged=nltk.pos_tag(words)
            print(tagged)
            
    except Exception as ex:
        print(str(ex))
        
process_i()

