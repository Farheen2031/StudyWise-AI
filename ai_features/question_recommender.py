"""
question_recommender.py

Generates exam-style important questions from study material
using TF-IDF keyword extraction.

Runs locally without any external AI API.
"""

from sklearn.feature_extraction.text import TfidfVectorizer


QUESTION_TEMPLATES = [
    "What is {kw}?",
    "Explain {kw} in detail.",
    "Define {kw} and give an example.",
    "Discuss the importance of {kw}.",
    "Describe the main features of {kw}.",
    "How does {kw} work?",
]


def extract_keywords(text, num_keywords=8):
    """Extract important keywords from the supplied text."""

    if not isinstance(text, str) or not text.strip():
        return []

    if not isinstance(num_keywords, int) or num_keywords <= 0:
        return []

    try:
        vectorizer = TfidfVectorizer(
            stop_words="english",
            max_features=50
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

    except Exception:
        return []


def generate_important_questions(text, num_questions=5):
    """Generate simple exam-style questions from important keywords."""

    if not isinstance(num_questions, int) or num_questions <= 0:
        return []

    keywords = extract_keywords(
        text,
        num_keywords=num_questions
    )

    questions = []

    for index, keyword in enumerate(keywords):
        template = QUESTION_TEMPLATES[
            index % len(QUESTION_TEMPLATES)
        ]

        questions.append(
            template.format(kw=keyword)
        )

    return questions


if __name__ == "__main__":
    sample_text = (
        "Photosynthesis is the process by which green plants "
        "convert sunlight into chemical energy. Chlorophyll "
        "absorbs sunlight and helps produce glucose and oxygen."
    )

    print("Important Questions:")

    for question in generate_important_questions(
        sample_text,
        num_questions=4
    ):
        print("-", question)