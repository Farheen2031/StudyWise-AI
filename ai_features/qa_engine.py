"""
qa_engine.py

Finds the most relevant sentences from study material
for a user's question using TF-IDF and cosine similarity.

Runs locally without any external AI API.
"""

import re

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def split_sentences(text):
    """Split study material into individual sentences safely."""

    if not isinstance(text, str) or not text.strip():
        return []

    text = text.replace("\n", " ").strip()

    sentences = re.split(r"(?<=[.!?])\s+", text)

    return [
        sentence.strip()
        for sentence in sentences
        if len(sentence.strip()) > 15
    ]


def answer_question(text, question, top_n=2):
    """
    Find the most relevant sentence(s) in the study material
    for the user's question.
    """

    if not isinstance(text, str) or not text.strip():
        return "No material available to search for an answer."

    if not isinstance(question, str) or not question.strip():
        return "Please enter a question."

    if not isinstance(top_n, int) or top_n <= 0:
        return "The number of answers must be greater than 0."

    sentences = split_sentences(text)

    if not sentences:
        return "No usable sentences were found in the study material."

    try:
        all_texts = sentences + [question.strip()]

        # No English-only stop words so the feature is
        # not unnecessarily restricted to English material.
        vectorizer = TfidfVectorizer(
            stop_words="english"
        )

        vectors = vectorizer.fit_transform(all_texts)

        question_vector = vectors[-1]
        sentence_vectors = vectors[:-1]

        similarities = cosine_similarity(
            question_vector,
            sentence_vectors
        )[0]

        number_of_answers = min(top_n, len(sentences))

        ranked_indices = similarities.argsort()[::-1][:number_of_answers]

        # Put selected sentences back in their original order.
        selected_indices = sorted(ranked_indices)

        best_score = similarities[ranked_indices[0]]

        # A very low score means the material probably
        # does not contain an answer to the question.
        if best_score < 0.10:
            return (
                "Sorry, I couldn't find a relevant answer in this "
                "material. Try rephrasing your question."
            )

        return " ".join(
            sentences[index]
            for index in selected_indices
        )

    except ValueError:
        return (
            "Sorry, I couldn't process this question. "
            "Please try different study material or rephrase the question."
        )

    except Exception:
        return "Sorry, an error occurred while finding the answer."


if __name__ == "__main__":
    sample_text = """
    Photosynthesis is the process by which green plants
    convert sunlight into chemical energy.
    Chlorophyll absorbs sunlight and helps convert
    carbon dioxide and water into glucose and oxygen.
    Plants release oxygen as a byproduct of photosynthesis.
    """

    question = "What produces oxygen?"

    print("Question:", question)
    print("Answer:", answer_question(sample_text, question))