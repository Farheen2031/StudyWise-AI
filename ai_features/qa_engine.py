"""
qa_engine.py
Answers a user's typed question by finding the most relevant sentence(s)
in the uploaded material using TF-IDF cosine similarity with n-grams.
"""

import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def split_sentences(text):
    # Normalize bullet characters into sentence breaks
    text = re.sub(r'[•●▪]', '\n', text)
    text = text.replace("\n", " . ")

    sentences = re.split(r'(?<=[.!?])\s+', text)
    return [s.strip() for s in sentences if len(s.strip()) > 15]


def answer_question(text, question, top_n=2):
    if not text or not isinstance(text, str) or not text.strip():
        return "No material available to search for an answer."
    if not question or not isinstance(question, str) or not question.strip():
        return "Please type a question."

    sentences = split_sentences(text)
    if not sentences:
        return "No material available to search for an answer."

    top_n = min(top_n, len(sentences))

    try:
        all_texts = sentences + [question]

        # ngram_range=(1,2) lets the model match short phrases like
        # "cosine similarity" or "TF-IDF", not just single words
        vectorizer = TfidfVectorizer(stop_words='english', ngram_range=(1, 2))
        vectors = vectorizer.fit_transform(all_texts)

        question_vector = vectors[-1]
        sentence_vectors = vectors[:-1]
        similarities = cosine_similarity(question_vector, sentence_vectors)[0]

        ranked_indices = similarities.argsort()[::-1][:top_n]

        # Drop any of the top picks that scored far below the best match,
        # so we don't pad the answer with weakly-related sentences
        best_score = similarities[ranked_indices[0]]
        if best_score < 0.05:
            return "Sorry, I couldn't find a relevant answer in this material. Try rephrasing your question."

        strong_indices = [
            i for i in ranked_indices
            if similarities[i] >= best_score * 0.5
        ]
        strong_indices = sorted(strong_indices)

        return " ".join(sentences[i] for i in strong_indices)

    except ValueError:
        return "Sorry, I couldn't process that question. Try rephrasing it."