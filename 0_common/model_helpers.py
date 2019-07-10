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

def plot_roc_curve(fpr, tpr, label=None):
    import matplotlib.pyplot as plt
    
    """
    The ROC curve, modified from 
    Hands-On Machine learning with Scikit-Learn and TensorFlow; p.91
    """
    plt.figure(figsize=(8,8))
    plt.title('ROC Curve')
    plt.plot(fpr, tpr, linewidth=2, label=label)
    plt.plot([0, 1], [0, 1], 'k--')
    plt.axis([-0.005, 1, 0, 1.005])
    plt.xticks(np.arange(0,1, 0.05), rotation=90)
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate (Recall)")
    plt.legend(loc='best')

    return plt