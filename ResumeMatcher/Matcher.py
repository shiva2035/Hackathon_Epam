import nltk, string
import os
from sklearn.feature_extraction.text import TfidfVectorizer

nltk.download('punkt')
stemmer = nltk.stem.SnowballStemmer("english")
remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)

def stem_tokens(tokens):
    return [stemmer.stem(item) for item in tokens]

'''remove punctuation, lowercase, stem'''
def normalize(text):
    return stem_tokens(nltk.word_tokenize(text.lower().translate(remove_punctuation_map)))

vectorizer = TfidfVectorizer(tokenizer=normalize, stop_words='english')

def cosine_sim(text1, text2):
    tfidf = vectorizer.fit_transform([text1, text2])
    return ((tfidf * tfidf.T).A)[0,1]


def matcher(desired_prfiles_path, profiles_path):
    for jd in os.listdir(desired_prfiles_path):
        jd_text = open(desired_prfiles_path+'/'+jd, 'r').read()
        for pr in os.listdir(profiles_path):
            pr_text = open(profiles_path+'/'+pr, 'r').read()
            match = cosine_sim(jd_text, pr_text)
            print("match between job description: " + str(jd) + " and profile: " + str(pr) + " is "+ str(match))

matcher('desired_profiles','profiles')