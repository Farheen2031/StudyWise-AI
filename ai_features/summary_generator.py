"""
summary_generator.py

Extractive text summarization using TF-IDF and TextRank.
Runs locally without any external AI API.
"""

import re

import networkx as nx
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def split_sentences(text):
    """Split text into simple sentences safely."""
    if not isinstance(text, str) or not text.strip():
        return []

    text = text.replace("\n", " ").strip()

    sentences = re.split(r"(?<=[.!?])\s+", text)

    return [
        sentence.strip()
        for sentence in sentences
        if len(sentence.strip()) > 20
    ]


def generate_summary(text, num_sentences=5):
    """
    Generate an extractive summary.

    The most important sentences are selected using
    TF-IDF sentence similarity and PageRank.
    """

    if not isinstance(text, str) or not text.strip():
        return "Not enough text to summarize."

    if not isinstance(num_sentences, int) or num_sentences <= 0:
        return "Number of summary sentences must be greater than 0."

    sentences = split_sentences(text)

    if not sentences:
        return "Not enough text to summarize."

    if len(sentences) <= num_sentences:
        return " ".join(sentences)

    try:
        # No English-only stop words so the feature is not
        # unnecessarily restricted to English study material.
        vectorizer = TfidfVectorizer()
        vectors = vectorizer.fit_transform(sentences)

        similarity_matrix = cosine_similarity(vectors)

        graph = nx.from_numpy_array(similarity_matrix)

        scores = nx.pagerank(graph)

        ranked = sorted(
            scores.items(),
            key=lambda item: item[1],
            reverse=True
        )

        selected_indices = sorted(
            index for index, _ in ranked[:num_sentences]
        )

        return " ".join(sentences[index] for index in selected_indices)

    except ValueError:
        return "The text does not contain enough usable information to summarize."

    except Exception:
        return "Sorry, the summary could not be generated."


if __name__ == "__main__":
    print("summary_generator.py is working.")