from sklearn.feature_extraction.text import TfidfVectorizer

def vectorize_text(data):
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(data['processed_description'])
    return tfidf_vectorizer, tfidf_matrix
