import nltk
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from faq_data import faq_pairs

# download once
# nltk.download('punkt')

def preprocess(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text

questions = [preprocess(f["question"]) for f in faq_pairs]
answers = [f["answer"] for f in faq_pairs]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(questions)

def get_response(user_input):
    user_input = preprocess(user_input)
    user_vec = vectorizer.transform([user_input])

    similarity = cosine_similarity(user_vec, X)
    index = similarity.argmax()
    score = similarity[0][index]

    if score < 0.25:
        return "Sorry, I couldn't understand your question. Please try again."

    return answers[index]