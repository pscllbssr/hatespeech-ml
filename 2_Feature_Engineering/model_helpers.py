import string
import re
import nltk

def clean_input(text): 
    stopwords = nltk.corpus.stopwords.words('german') 
    lm = nltk.WordNetLemmatizer()
    
    # todo: remove user hashes in comment text with "@" and without    
    text = "".join([word.lower() for word in text if word not in string.punctuation])
    tokens = re.split('\W+', text)
    text = [lm.lemmatize(word) for word in tokens if word not in stopwords]
    return " ".join(text)