import nltk
import spacy
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer

# nltk.download('punkt')
# nltk.download('stopwords')

docs = [
    'I love NLP',
    'He went to college'
]

stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()

processed_docs = []

for doc in docs:
    tokens = word_tokenize(doc.lower())
    filtered = [t for t in tokens if t not in stop_words]
    stemmed = [stemmer.stem(t) for t in filtered]
    processed_docs.append(" ".join(stemmed))

vectorizer = CountVectorizer()
data = vectorizer.fit_transform(processed_docs)

print("Vocabulary:", vectorizer.get_feature_names_out())
print("Bag of Words:\n", data.toarray())


nlp = spacy.load("en_core_web_sm")

for sentence in docs:
    doc = nlp(sentence)
    sub = verb = obj = None

    for token in doc:
        if token.dep_ == "nsubj":
            sub = token.text
        elif token.pos_ == "VERB":
            verb = token.text
        elif token.dep_ in ("dobj", "pobj"):
            obj = token.text

    print(f"{sub} -> {verb} -> {obj}")


