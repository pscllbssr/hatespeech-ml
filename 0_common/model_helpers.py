import string
import re
import nltk

# remove stopwords, tokenize words an lemmatize
def clean_input(text): 
    stopwords = nltk.corpus.stopwords.words('german') 
    lm = nltk.WordNetLemmatizer()
    
    # todo: remove user hashes in comment text with "@" and without    
    text = "".join([word.lower() for word in text if word not in string.punctuation])
    tokens = re.split('\W+', text)
    text = [lm.lemmatize(word) for word in tokens if word not in stopwords]
    return " ".join(text)

# twitter specific cleanup
def clean_tweet(text):
    text = re.sub(r'http\S+', '', text) # links
    text = re.sub(r'^[a-f0-9]{16}', '', text) # user hashes
    text = re.sub(r'@(\w+)',  '', text) # usernames
    text = re.sub(r'RT',  '',text) # RT --> retweets
    return text

def clean_all(text):
    text = clean_tweet(text)
    text = clean_input(text)
    return text