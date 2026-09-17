"""
mcq_generator.py

Generates simple fill-in-the-blank multiple-choice questions
from study material using TF-IDF keyword extraction.
"""

import random
import re

from sklearn.feature_extraction.text import TfidfVectorizer


def split_sentences(text):
    """Split study material into usable sentences."""
    if not isinstance(text, str):
        return []

    text = text.replace("\n", " ").strip()

    sentences = re.split(r"(?<=[.!?])\s+", text)

    return [
        sentence.strip()
        for sentence in sentences
        if 30 <= len(sentence.strip()) <= 300
    ]


def extract_keywords(text, num_keywords=20):
    """Extract important keywords using TF-IDF."""
    if not isinstance(text, str) or not text.strip():
        return []

    try:
        vectorizer = TfidfVectorizer(
            stop_words="english",
            max_features=50,
            token_pattern=r"(?u)\b[a-zA-Z][a-zA-Z-]{2,}\b"
        )

        vectors = vectorizer.fit_transform([text])

        scores = vectors.toarray()[0]
        terms = vectorizer.get_feature_names_out()

        ranked = sorted(
            zip(scores, terms),
            key=lambda item: item[0],
            reverse=True
        )

        return [
            term
            for score, term in ranked[:num_keywords]
            if score > 0
        ]

    except ValueError:
        return []


def generate_mcqs(text, num_questions=5):
    """Generate fill-in-the-blank MCQs."""
    if not isinstance(text, str) or not text.strip():
        return []

    if num_questions <= 0:
        return []

    sentences = split_sentences(text)
    keywords = extract_keywords(text, num_keywords=30)

    if not sentences or not keywords:
        return []

    mcqs = []
    used_sentences = set()

    for keyword in keywords:
        if len(mcqs) >= num_questions:
            break

        for index, sentence in enumerate(sentences):

            if index in used_sentences:
                continue

            pattern = r"\b" + re.escape(keyword) + r"\b"

            if not re.search(pattern, sentence, re.IGNORECASE):
                continue

            blanked_sentence = re.sub(
                pattern,
                "_____",
                sentence,
                count=1,
                flags=re.IGNORECASE
            )

            # Use other extracted keywords as distractors.
            distractors = [
                word for word in keywords
                if word.lower() != keyword.lower()
            ]

            random.shuffle(distractors)

            options = [keyword] + distractors[:3]

            # Only use four options when possible.
            options = list(dict.fromkeys(options))

            if len(options) < 4:
                continue

            options = options[:4]
            random.shuffle(options)

            mcqs.append(
                {
                    "question": f"Fill in the blank: {blanked_sentence}",
                    "options": options,
                    "correct_answer": keyword,
                }
            )

            used_sentences.add(index)
            break

    return mcqs