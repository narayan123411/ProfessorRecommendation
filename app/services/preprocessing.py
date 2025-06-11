import re
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))

def preprocess_text(text):
    text = re.sub(r'\W+', ' ', str(text).lower())
    return ' '.join([word for word in text.split() if word not in stop_words])
